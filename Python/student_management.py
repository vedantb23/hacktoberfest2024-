import json

# File to store student data
DATA_FILE = 'students.json'

# Load student data from the JSON file
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save student data to the JSON file
def save_data(students):
    with open(DATA_FILE, 'w') as file:
        json.dump(students, file, indent=4)

# Add a new student
def add_student(students):
    roll_no = input("Enter roll number: ")
    if roll_no in students:
        print("Student with this roll number already exists!")
        return
    name = input("Enter student's name: ")
    marks = float(input("Enter marks: "))
    students[roll_no] = {'name': name, 'marks': marks}
    print(f"Student {name} added successfully!")

# View all students
def view_students(students):
    if not students:
        print("No students found!")
    else:
        print(f"{'Roll No':<10} {'Name':<20} {'Marks':<10}")
        print("-" * 40)
        for roll_no, details in students.items():
            print(f"{roll_no:<10} {details['name']:<20} {details['marks']:<10}")

# Update student details
def update_student(students):
    roll_no = input("Enter roll number of the student to update: ")
    if roll_no not in students:
        print("Student not found!")
        return
    name = input("Enter new name: ")
    marks = float(input("Enter new marks: "))
    students[roll_no] = {'name': name, 'marks': marks}
    print(f"Student {name} updated successfully!")

# Delete a student
def delete_student(students):
    roll_no = input("Enter roll number of the student to delete: ")
    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

# Main menu
def main():
    students = load_data()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            save_data(students)
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
