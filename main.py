# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_course_info():
    gpa_list = []
    all_gpa_entered = False
    course_info = []

    while not all_gpa_entered:
        course_name = input("Enter the course name or code: ")
        course_grade = input("Enter your GPA in the course (gpa or letter grade): ")
        course_weight = input("Enter the GPA weight of the course: ")

        course_info.append(course_name)
        course_info.append(course_grade)
        course_info.append(course_weight)

        gpa_list.append(course_info)

        course_info = []

        valid_input = False

        while not valid_input:

            user_decision = input("Do you want to add another course [y/n]: ")
            print()

            if user_decision[0].lower() == "y":
                valid_input = True
            elif user_decision[0].lower() == "n":
                valid_input = True
                all_gpa_entered = True
            else:
                print("Please enter a valid input [y/n]")

    for i in range(0, len(gpa_list)):
        print(gpa_list[i])

    return gpa_list


def calculate_gpa(gpa_list):
    total_gpa_sum = 0.0
    total_weight_sum = 0.0

    for i in range(0, len(gpa_list)):
        total_gpa_sum += float(gpa_list[i][1]) * float(gpa_list[i][2])
        total_weight_sum += float(gpa_list[i][2])

    return total_gpa_sum / total_weight_sum


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    course_data = get_course_info()
    gpa = calculate_gpa(course_data)
    print("your GPA is", format(gpa, ".2f"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
