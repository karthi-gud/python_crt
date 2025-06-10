Manual Setup Guide - Movie Recommendation System
This guide provides step-by-step instructions to manually set up and run the Joint Movie Recommendation System on your local machine.

Prerequisites
Python 3.8 or higher
pip (Python package installer)
Git (optional)
Step 1: Create Project Directory
mkdir joint-movie-recommendation-system
cd joint-movie-recommendation-system
Step 2: Create Virtual Environment (Recommended)
# Create virtual environment
python -m venv movie_rec_env
# Activate virtual environment
# On Windows:
movie_rec_env\Scripts\activate
# On macOS/Linux:
source movie_rec_env/bin/activate
Step 3: Install Required Packages
pip install streamlit==1.28.0
pip install pandas==2.0.3
pip install numpy==1.24.3
pip install matplotlib==3.7.2
pip install matplotlib-venn==0.11.9
pip install seaborn==0.12.2
pip install psycopg2-binary==2.9.7
pip install sqlalchemy==2.0.19
Step 4: Download MovieLens Dataset
Go to https://grouplens.org/datasets/movielens/100k/
Download ml-100k.zip
Extract the zip file
Create a data folder in your project directory
Copy u.data and u.item from the extracted folder to your data folder
Your directory structure should look like:

joint-movie-recommendation-system/
├── data/
│   ├── u.data
│   └── u.item
└── (Python files will go here)
Step 5: Create Application Files
Save each of the following files in your project directory:

File 1: requirements.txt
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
matplotlib-venn>=0.11.0
seaborn>=0.12.0
psycopg2-binary>=2.9.0
sqlalchemy>=2.0.0
File 2: .streamlit/config.toml
Create a .streamlit folder and inside it create config.toml:

[server]
headless = true
address = "0.0.0.0"
port = 8501
Step 6: Database Setup (Optional)
If you want to use PostgreSQL database features:

Install PostgreSQL
Windows: Download from https://www.postgresql.org/download/windows/
macOS: brew install postgresql
Ubuntu/Debian: sudo apt-get install postgresql postgresql-contrib
Create Database
-- Connect to PostgreSQL as superuser
psql -U postgres
-- Create database
CREATE DATABASE movie_recommendations;
-- Create user (optional)
CREATE USER movie_user WITH ENCRYPTED PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE movie_recommendations TO movie_user;
-- Exit psql
\q
Set Environment Variable
# Windows (Command Prompt)
set DATABASE_URL=postgresql://postgres:your_password@localhost:5432/movie_recommendations
# Windows (PowerShell)
$env:DATABASE_URL="postgresql://postgres:your_password@localhost:5432/movie_recommendations"
# macOS/Linux
export DATABASE_URL="postgresql://postgres:your_password@localhost:5432/movie_recommendations"
Step 7: Run the Application
# Make sure you're in the project directory
cd joint-movie-recommendation-system
# Run the Streamlit application
streamlit run app.py
The application will open in your browser at http://localhost:8501

Step 8: Using the Application
Click "Load Dataset" to initialize the MovieLens data
Select two users from the dropdown menus
View user profiles and recommendations
Explore visualizations and insights
Troubleshooting
Common Issues:
1. Module Import Errors

# Ensure all packages are installed
pip install -r requirements.txt
2. Dataset Not Found

Verify u.data and u.item files are in the data/ folder
Check file permissions
3. Database Connection Issues

Verify PostgreSQL is running
Check DATABASE_URL format
Ensure database and user exist
4. Port Already in Use

# Use different port
streamlit run app.py --server.port 8502
Performance Tips:
Memory Usage: For large datasets, consider using database mode
Startup Time: Database initialization may take 1-2 minutes on first run
Recommendations: Generation time depends on user activity levels
Alternative: Docker Setup
If you prefer Docker:

Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
Build and Run
docker build -t movie-recommendation .
docker run -p 8501:8501 movie-recommendation
Production Deployment
For production deployment, consider:

Environment Variables: Use .env files for configuration
Database: Use managed PostgreSQL service
Scaling: Deploy on cloud platforms (Heroku, AWS, GCP)
Security: Implement authentication and HTTPS
Monitoring: Add logging and error tracking
Development Mode
For development with auto-reload:

streamlit run app.py --server.runOnSave true
File Structure Summary
Your final project structure should be:

joint-movie-recommendation-system/
├── .streamlit/
│   └── config.toml
├── data/
│   ├── u.data
│   └── u.item
├── app.py
├── data_loader.py
├── recommendation_engine.py
├── visualizations.py
├── database_manager.py
├── requirements.txt
└── README.md
Support
If you encounter issues:

Check the console for error messages
Verify all dependencies are installed
Ensure MovieLens data files are properly placed
Check database configuration if using PostgreSQL
The application is now ready to run on your local system!