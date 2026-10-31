"""Main menu for the Student Performance Analytics System."""
from functions import (
    load_student_data, calculate_results, show_subject_analysis,
    show_class_summary, show_top_students, show_student_details
)

def main():
    print("=" * 62)
    print("          STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 62)

    try:
        raw_data = load_student_data("students.csv")
        data = calculate_results(raw_data)
    except (FileNotFoundError, ValueError) as error:
        print("Unable to start the project:", error)
        return

    print(f"Successfully loaded {len(data)} student records.")

    while True:
        print("\nMAIN MENU")
        print("1. Display all student results")
        print("2. Search student by ID")
        print("3. Show subject-wise analysis")
        print("4. Show class summary")
        print("5. Show top 5 students")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            columns = ["Student_ID", "Name", "Department", "Total",
                       "Average", "Grade", "Result", "Attendance"]
            print("\nALL STUDENT RESULTS")
            print(data[columns].to_string(
                index=False, formatters={"Average": "{:.2f}".format}
            ))
        elif choice == "2":
            show_student_details(data)
        elif choice == "3":
            show_subject_analysis(data)
        elif choice == "4":
            show_class_summary(data)
        elif choice == "5":
            show_top_students(data)
        elif choice == "6":
            print("Thank you for using the Student Performance Analytics System!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
