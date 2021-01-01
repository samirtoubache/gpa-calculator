# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import userInput


def calculate_gpa(gpa_list):
    total_gpa_sum = 0.0
    total_weight_sum = 0.0

    for i in range(0, len(gpa_list)):
        total_gpa_sum += float(gpa_list[i][1]) * float(gpa_list[i][2])
        total_weight_sum += float(gpa_list[i][2])

    return total_gpa_sum / total_weight_sum


def main():
    gpa_scale = userInput.get_gpa_scale()

    course_data = userInput.get_course_info(gpa_scale)

    while True:

        decision = input("Please select one of the following options:\n[1] Calculate GPA, [2] View Courses, [3] modify "
                         "course list, [4] Exit Application: ")

        if int(decision) == 1:
            gpa = calculate_gpa(course_data)
            print("your GPA is", format(gpa, ".2f"))
        elif int(decision) == 2:
            print("\nHere is a list of the courses you entered:")
            userInput.print_courses(course_data)
        elif int(decision) == 3:
            modify_choice = input("Would you like to add or remove a course? [1] Add course, [2] Remove Course: ")
            if int(modify_choice) == 1:
                course_data.append(userInput.add_course(gpa_scale))
            elif int(modify_choice) == 2:
                course_data = userInput.remove_course(course_data)
        elif int(decision) == 4:
            print("Thank you for using this application, Exiting Script...")
            exit(0)
        else:
            print("Please select a valid option.")


if __name__ == '__main__':
    main()
