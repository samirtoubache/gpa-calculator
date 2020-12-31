# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from userInput import get_course_info


def calculate_gpa(gpa_list):
    total_gpa_sum = 0.0
    total_weight_sum = 0.0

    for i in range(0, len(gpa_list)):
        total_gpa_sum += float(gpa_list[i][1]) * float(gpa_list[i][2])
        total_weight_sum += float(gpa_list[i][2])

    return total_gpa_sum / total_weight_sum


def main():
    course_data = get_course_info()
    gpa = calculate_gpa(course_data)
    print("your GPA is", format(gpa, ".2f"))


if __name__ == '__main__':
    main()
