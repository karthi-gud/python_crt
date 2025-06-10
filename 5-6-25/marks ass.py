#write a python program to read marks of 5 students for three subjecs each and prijnt the marks list for individual student along with the class where
#if student got more than 90% first class
# if student got more than 75% second class
# if student got more than 50% third class 
#and fail if it is less than 50%
marks = []
for i in range(5):
    student_marks = []
    for j in range(3):
        mark = float(input(f"Enter marks for Student {i + 1}, Subject {j + 1}: "))
        student_marks.append(mark)
    marks.append(student_marks)
for i, student_marks in enumerate(marks):
    total_marks = sum(student_marks)
    percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100
    if percentage > 90:
        class_status = "First Class"
    elif percentage > 75:
        class_status = "Second Class"
    elif percentage > 50:
        class_status = "Third Class"
    else:
        class_status = "Fail"
    
    print(f"Student {i + 1} Marks: {student_marks}, Percentage: {percentage:.2f}%, Class: {class_status}")
    
# Example input for marks:
# Student 1: 95, 85, 90
# Student 2: 70, 75, 80
# Student 3: 50, 60, 55
# Student 4: 40, 45, 30
# Student 5: 80, 90, 85
# Example output:
# Student 1 Marks: [95.0, 85.0, 90.0], Percentage: 90.00%, Class: First Class
# Student 2 Marks: [70.0, 75.0, 80.0], Percentage: 75.00%, Class: Second Class
# Student 3 Marks: [50.0, 60.0, 55.0], Percentage: 55.00%, Class: Third Class
# Student 4 Marks: [40.0, 45.0, 30.0], Percentage: 38.33%, Class: Fail
#write a python program to read a list of numbers from the user and print the list of elements which are multiples of 3 and 5

