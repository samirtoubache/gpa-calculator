
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


def get_course_info():
    gpa_list = []
    all_gpa_entered = False
    course_info = []

    gpa_scale = get_gpa_scale()

    print("Enter all courses you want to include in you GPA calculation with their corresponding grades.\n")

    while not all_gpa_entered:
        course_name = input("Enter the course name or code: ")
        course_grade = input("Enter your GPA in the course (gpa or letter grade): ")
        course_weight = input("Enter the GPA weight of the course: ")

        if not course_grade.isdigit():
            course_grade = gpa_scale[course_grade]

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

    return gpa_list
