
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