from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from functools import wraps
from typing import List, Optional
import csv
import io

app = Flask(__name__)
app.secret_key = "notion_clone_secret"
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'tasks.db')
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
# --- Custom Decorator for Logging ---
def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Action: {func.__name__} called")
        return func(*args, **kwargs)
    return wrapper

# --- Section Model (Inheritance Example) ---
class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tasks = db.relationship('Task', backref='section', lazy=True)

# --- Association Table for Tags ---
task_tags = db.Table('task_tags',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

# --- Tag Model ---
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

# --- Task Model ---
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.String(20), nullable=True)
    priority = db.Column(db.String(10), nullable=True)
    status = db.Column(db.String(10), default='Pending')
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=True)
    tags = db.relationship('Tag', secondary=task_tags, backref=db.backref('tasks', lazy='dynamic'))

    def mark_complete(self):
        self.status = 'Completed'

    def update_details(self, title: str, description: str, due_date: str, priority: str, section_id: Optional[int], tag_ids: List[int]):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.section_id = section_id
        self.tags = [Tag.query.get(tid) for tid in tag_ids if Tag.query.get(tid)]

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    sort_by = request.args.get('sort', 'due_date')
    search = request.args.get('search', '')
    section_id = request.args.get('section', type=int)
    tag_id = request.args.get('tag', type=int)
    query = Task.query

    if search:
        query = query.filter(Task.title.contains(search) | Task.description.contains(search))
    if section_id:
        query = query.filter(Task.section_id == section_id)
    if tag_id:
        query = query.filter(Task.tags.any(Tag.id == tag_id))

    if sort_by == 'priority':
        tasks = query.order_by(Task.priority).all()
    else:
        tasks = query.order_by(Task.due_date).all()

    sections = Section.query.all()
    tags = Tag.query.all()
    return render_template('index.html', tasks=tasks, sections=sections, tags=tags, sort_by=sort_by, search=search, section_id=section_id, tag_id=tag_id)

@app.route('/add', methods=['POST'])
@log_action
def add_task():
    try:
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']
        section_id = request.form.get('section_id', type=int)
        tag_ids = request.form.getlist('tags', type=int)
        task = Task(title=title, description=description, due_date=due_date, priority=priority, section_id=section_id)
        task.tags = [Tag.query.get(tid) for tid in tag_ids if Tag.query.get(tid)]
        db.session.add(task)
        db.session.commit()
        flash("Task added!", "success")
    except Exception as e:
        flash(f"Error adding task: {e}", "danger")
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
@log_action
def delete_task(task_id):
    try:
        task = Task.query.get(task_id)
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted!", "info")
    except Exception as e:
        flash(f"Error deleting task: {e}", "danger")
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
@log_action
def complete_task(task_id):
    try:
        task = Task.query.get(task_id)
        task.mark_complete()
        db.session.commit()
        flash("Task marked as complete!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['POST'])
@log_action
def edit_task(task_id):
    try:
        task = Task.query.get(task_id)
        section_id = request.form.get('section_id', type=int)
        tag_ids = request.form.getlist('tags', type=int)
        task.update_details(
            request.form['title'],
            request.form['description'],
            request.form['due_date'],
            request.form['priority'],
            section_id,
            tag_ids
        )
        db.session.commit()
        flash("Task updated!", "success")
    except Exception as e:
        flash(f"Error updating task: {e}", "danger")
    return redirect(url_for('index'))

@app.route('/add_section', methods=['POST'])
def add_section():
    name = request.form['section_name']
    db.session.add(Section(name=name))
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_tag', methods=['POST'])
def add_tag():
    name = request.form['tag_name']
    if not Tag.query.filter_by(name=name).first():
        db.session.add(Tag(name=name))
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/export')
def export_tasks():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Title', 'Description', 'Due Date', 'Priority', 'Status', 'Section', 'Tags'])
    for task in Task.query.all():
        tags = ','.join([tag.name for tag in task.tags])
        section = task.section.name if task.section else ''
        writer.writerow([task.title, task.description, task.due_date, task.priority, task.status, section, tags])
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv', as_attachment=True, download_name='tasks.csv')

if __name__ == '__main__':
    app.run(debug=True)