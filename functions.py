"""Reusable functions for the Student Performance Analytics System."""
import numpy as np
import pandas as pd

SUBJECTS = ["Maths", "Science", "English", "Computer"]

def load_student_data(file_path="students.csv"):
    """Load student records from a CSV file into a Pandas DataFrame."""
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Could not find '{file_path}'. Keep students.csv in the same folder as main.py."
        )
    required = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance"]
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError("CSV is missing these required columns: " + ", ".join(missing))
    if data.empty:
        raise ValueError("The student dataset is empty.")
    return data

def calculate_results(data):
    """Return a copy of the data with total, average, grade and pass/fail columns."""
    result = data.copy()
    result["Total"] = result[SUBJECTS].sum(axis=1)
    result["Average"] = result["Total"] / len(SUBJECTS)

    def grade_from_average(average):
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    result["Grade"] = result["Average"].apply(grade_from_average)

    # A student passes only when every subject mark is at least 35.
    result["Result"] = np.where((result[SUBJECTS] >= 35).all(axis=1), "Pass", "Fail")
    return result

def show_subject_analysis(data):
    """Display average, highest and lowest marks for every subject."""
    print("\nSUBJECT-WISE PERFORMANCE")
    print("-" * 62)
    for subject in SUBJECTS:
        marks = data[subject].to_numpy()
        print(
            f"{subject:<12} Average: {np.mean(marks):6.2f} | "
            f"Highest: {np.max(marks):3.0f} | Lowest: {np.min(marks):3.0f}"
        )

def show_class_summary(data):
    """Display overall class statistics."""
    passed = int((data["Result"] == "Pass").sum())
    failed = int((data["Result"] == "Fail").sum())
    print("\nCLASS SUMMARY")
    print("-" * 40)
    print(f"Number of students : {len(data)}")
    print(f"Class average      : {data['Average'].mean():.2f}")
    print(f"Highest average    : {data['Average'].max():.2f}")
    print(f"Lowest average     : {data['Average'].min():.2f}")
    print(f"Students passed    : {passed}")
    print(f"Students failed    : {failed}")
    print(f"Average attendance: {data['Attendance'].mean():.2f}%")

def show_top_students(data, count=5):
    """Display students ranked by average marks."""
    print(f"\nTOP {count} PERFORMING STUDENTS")
    print("-" * 62)
    top = data.nlargest(count, "Average")
    print(top[["Student_ID", "Name", "Department", "Average", "Grade"]].to_string(
        index=False, formatters={"Average": "{:.2f}".format}
    ))

def show_student_details(data):
    """Find and display one student's result using their ID."""
    raw_id = input("Enter Student ID: ").strip()
    if not raw_id.isdigit():
        print("Please enter a numeric Student ID.")
        return
    student = data[data["Student_ID"] == int(raw_id)]
    if student.empty:
        print("No student found with that ID.")
        return
    print("\nSTUDENT RESULT")
    print("-" * 40)
    print(student[["Student_ID", "Name", "Department", *SUBJECTS,
                   "Total", "Average", "Grade", "Result", "Attendance"]]
          .to_string(index=False, formatters={"Average": "{:.2f}".format}))
