# Project Documentation

## 1. Project Title
**Student Performance Analytics System**

Student Name: ____________________  
Student ID: ____________________  
Course: Python with AI

## 2. Objective
The objective is to build a Python application that reads student marks and attendance, analyzes academic performance, and presents clear summaries to help understand individual and class performance.

## 3. Technologies Used
- Python
- NumPy
- Pandas
- CSV dataset

## 4. Dataset Description
The sample dataset contains 20 student records. Each record includes Student ID, Name, Department, marks in Maths, Science, English and Computer, and Attendance percentage.

## 5. Implementation
1. `pandas.read_csv()` loads the CSV file into a DataFrame.
2. A reusable function checks that the required columns exist.
3. Pandas calculates total and average marks for each student.
4. A function with conditional statements assigns grades.
5. NumPy checks whether each student scored at least 35 in every subject and calculates subject statistics.
6. The menu uses a `while` loop and `if/elif` conditions to let the user select an analysis.
7. Functions display individual results, subject analysis, class summary and top performers.

## 6. Key Features
- View all student results.
- Search for a student using Student ID.
- Calculate total, average and grade.
- Identify pass/fail students.
- Compare subject-wise performance.
- Find the top five students.
- Calculate class average and attendance summary.

## 7. Output / Screenshots
After running `python main.py`, capture screenshots of:
- The main menu.
- All student results.
- Subject-wise analysis.
- Class summary.
- Top five students.

Paste your own screenshots here before submission.

## 8. Final Outcome
The project reads the supplied dataset and generates student-level and class-level performance summaries through a simple menu-driven Python program.

## 9. Challenges & Learning
Write about the actual challenges you faced while installing libraries, preparing the CSV file, debugging the program, and understanding Pandas and NumPy. Mention how you solved them. Personalize this section based on your own experience.

## 10. GitHub Repository
Repository URL: ______________________________________

## Calculation Rules
- Each subject is out of 100.
- Pass means at least 35 marks in every subject.
- Grade is based on average: A+ (90 and above), A (80–89.99), B (70–79.99), C (60–69.99), D (50–59.99), F (below 50).
- Attendance is reported separately and does not affect pass/fail status.
