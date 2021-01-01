
scale_43 = {
    "A+": 4.3,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "D-": 0.7,
    "F": 0
}


def print_gpa_scale():
    print("4.3 GPA Scale:")
    for key in scale_43:
        print(key, '->', scale_43[key])

    print()


def get_gpa_scale():

    while True:
        scale = input("Pick which GPA scale you want to use: [1] 4.3 scale, [2] view gpa scales: ")
        if int(scale) == 1:
            return scale_43
        elif int(scale) == 2:
            print_gpa_scale()
        else:
            print("Please enter a valid option.")


def add_course(gpa_scale):

    course_info = []
    course_name = input("Enter the course name or code: ")
    course_grade = input("Enter your GPA in the course (gpa or letter grade): ")
    course_weight = input("Enter the GPA weight of the course: ")

    if not course_grade.replace(".", "").isdigit():
        course_grade = gpa_scale[course_grade]

    course_info.append(course_name)
    course_info.append(course_grade)
    course_info.append(course_weight)

    print()

    return course_info


def get_course_info(gpa_scale):
    gpa_list = []
    all_gpa_entered = False

    print("Enter all courses you want to include in you GPA calculation with their corresponding grades.\n")

    while not all_gpa_entered:

        course_info = add_course(gpa_scale)
        gpa_list.append(course_info)

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

    return gpa_list


def remove_course(course_list):

    # if course list is empty
    if not course_list:
        print("Your course list is already empty, please add some courses.\n")
        return course_list

    print("Here are the courses that you already entered:\n")
    print_courses(course_list)
    delete_course = input("Enter the name of the course you want to remove: ")

    course_found = False
    for i in range(0, len(course_list)):
        if course_list[i][0].lower() == delete_course.lower():
            del course_list[i]
            course_found = True
            print(delete_course, "was removed from the course list")
            break

    if not course_found:
        print(delete_course + " was not found in your course list\n")

    return course_list


def print_courses(course_list):

    # if course list is empty
    if not course_list:
        print("Your course list is already empty, please add some courses.\n")
        return

    for course in course_list:
        print(str(course[0]) + ": GPA = " + str(course[1]) + ", weight = " + str(course[2]))

    print()
