import os
import numpy as np

# Function to view course information
def viewCourse(courses):
    while True:
        print("\n--- Courses Available ---")  # Display the "Courses Available" header
        for i, course in enumerate(courses, start=1):
            print(f"{i}: {course['key']}")

        print("\n----------------\n")
        x = input("Enter course number to view info:\nEnter -1 to go back to the main menu: ")

        # Check if the input is "-1" to go back to the main menu
        if x == "-1":
            print("Going back to the main menu.")
            break

        # Check if the input is numeric and within the valid range
        if x.isnumeric():
            x = int(x)
            if 1 <= x <= len(courses):
                sel_course = courses[x - 1]  # Adjusted index to access the correct course
                course_title = sel_course['key']
                print("\n" + course_title.upper())

                course_items_to_display = list(sel_course.keys())[1:]  # Exclude the "key" item
                while True:
                    print("\n----------------\n")
                    for j, val in enumerate(course_items_to_display, start=1):
                        print(f"{j}: {val}")

                    y = int(input("Select Info to be shown:\nEnter -1 to go back to the main menu: "))
                    if y == -1:
                        print("Going back to the main menu.")
                        break
                    elif 1 <= y <= len(course_items_to_display):
                        selected_key = course_items_to_display[y - 1]  # Adjusted index to access the correct item
                        print("\n------ " + selected_key + " -------\n")
                        print(sel_course[selected_key])
                    else:
                        print("Invalid selection.")
            else:
                print("Please enter a valid course number.")
        else:
            print("Please enter a valid number or -1 to go back to the main menu")

# Definition of the pupil class
class pupil:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.course = ""
        self.grades = []

# Definition of the register class
class register:
    def __init__(self, courses):
        self.pupils = []
        self.course_keys = [x['key'] for x in courses]

    def register_pupils(self):
        p = pupil()
        p.id = input("Enter ID: ")
        p.name = input("Enter Name: ")
        print("\n--- Courses Available ---")  # Display the "Courses Available" title
        for idx, k in enumerate(self.course_keys, start=1):
            print(f"{idx}: {k}")

        try:
            num = int(input("Enter Course number: "))
            if 1 <= num <= len(self.course_keys):
                p.course = self.course_keys[num - 1]
                print("\n------------- Registered\n")
                self.pupils.append(p)
            else:
                print("Enter a valid course number. Registration failed.")
        except ValueError:
            print("Invalid input. Registration failed.")

    # Method to grade a pupil
    def grade_pupil(self):
        pupil_id = input("Enter the ID of the pupil to grade: ")
        found_pupil = None
        for p in self.pupils:
            if p.id == pupil_id:
                found_pupil = p
                break
        if found_pupil is None:
            print("Pupil not found.")
            return

        print("Enter grades (0-100) for the pupil:")
        for x in range(1, 9):
            try:
                grade = int(input(f"Enter grade for unit no {x}: "))
                if 0 <= grade <= 100:
                    found_pupil.grades.append(grade)  # Append grades to existing list
                else:
                    print("Invalid grade. Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        print("Grades updated.")

    # Method to display pupil progress
    def display_grades(self):
        for p in self.pupils:
            sum = 0
            res = ""
            for x in p.grades:
                sum += int(x)
            sum = sum / 8
            if sum > 79:
                res = "Inspiring"
            elif sum > 60:
                res = "Distinction"
            elif sum > 50:
                res = "Merit"
            elif sum > 40:
                res = "Pass"
            else:
                res = "Fail"

            print("\n---------------\n")
            print(f"Name: {p.name}")  # Display the pupil's name
            print(f"ID: {p.id}")      # Display the pupil's provided ID
            print(f"Average Grade: {sum}")
            print(f"Result: {res}\n")

            # Display grades with unit numbers
            print("Grades for each unit:")
            for unit_num, grade in enumerate(p.grades, start=1):
                print(f"Unit {unit_num}: {grade}")

# Function to read course data from files
def read():
    c = []
    fnames = os.listdir("files")
    for name in fnames:
        t_dict = {}
        with open(os.path.join("files", name), "r") as f:
            data = f.read()
            for items in (data.split("---")):
                if items:
                    try:
                        k, v = items.split("~~")
                        t_dict[k] = v
                    except ValueError:
                        print("Error parsing data:", items)
        c.append(t_dict)
    return c

# Function to generate sample pupil data
def samplepupils():
    sample = []
    for x in range(8):
        p = pupil()
        p.id = "00" + str(x)
        p.name = "Sample" + str(x)
        for _ in range(8):
            p.grades.append(np.random.randint(0, 100))
        sample.append(p)
    return sample

# Main function to manage the course management system
def main():
    courses = read()
    sample_data = samplepupils()

    r = register(courses)
    x = 0
    while x != -1:
        print("\n--- Welcome to Course Management System ---")  # Display the welcome message
        print("Select an option:")
        print("1: View Courses")
        print("2: Register Pupil")
        print("3: Grade Pupil")
        print("4: Display Progress")
        print("-1: Exit")
        x = input("Enter your choice: ")

        # Check if the input is "-1" to exit
        if x == "-1":
            exit_choice = input("Are you sure you want to exit? (yes/no): ")
            if exit_choice.lower() == "yes":
                print("Thanks for using our Course Management System. Goodbye!")
                break
            elif exit_choice.lower() == "no":
                continue  # Stay in the main menu
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        elif x.isnumeric():
            x = int(x)
            if x == 1:
                viewCourse(courses)
            elif x == 2:
                r.register_pupils()  # Call the register_pupils method on the register instance
            elif x == 3:
                r.grade_pupil()
            elif x == 4:
                r.display_grades()
            else:
                print("Enter a valid number.")
        else:
            print("Enter a valid number or -1 to exit.")


