# student_information = {}
# while True:
#     information = input()
#     if information == "end":
#         break
#     current_information = information.split(" : ")
#     course = current_information[0]
#     student = current_information[1]
#     if course not in student_information.keys():
#         student_information[course] = []
#     student_information[course].append(student)
#
#
# for course_name, registered_students in student_information.items():
#     print(f"{course_name}: {len(registered_students)}")
#     for registered_students in sorted(registered_students):
#         print(f"-- {registered_students}")



def course_registration():
    courses = {}

    while True:
        entry = input()
        if entry == "end":
            break

        course_name, student_name = entry.split(" : ")

        if course_name not in courses:
            courses[course_name] = []

        courses[course_name].append(student_name)

    sorted_courses = sorted(courses.items(), key=lambda x: len(x[1]), reverse=True)

    for course, students in sorted_courses:
        print(f"{course}: {len(students)}")
        for student in sorted(students):
            print(f"-- {student}")


# Example usage:
course_registration()