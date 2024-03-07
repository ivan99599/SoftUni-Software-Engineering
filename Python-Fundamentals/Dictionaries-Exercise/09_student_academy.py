# lines = int(input())
# academy = {}
# for line in range(lines):
#     student_name = input()
#     student_grade = float(input())
#     if student_grade >= 4.5:
#         if student_name not in academy.keys():
#             academy[student_name] = []
#         academy[student_name].append(student_grade)
#
#
# for name, grade in academy.items():
#     print(f"{name} -> {sum(grade) // len(grade)}")


def student_academy():
    num_students = int(input())
    students_data = {}

    for _ in range(num_students):
        student_name = input()
        grade = float(input())

        if student_name not in students_data:
            students_data[student_name] = []

        students_data[student_name].append(grade)

    filtered_students = {name: sum(grades) / len(grades) for name, grades in students_data.items() if sum(grades) / len(grades) >= 4.5}

    sorted_students = sorted(filtered_students.items(), key=lambda x: -x[1])

    for name, average_grade in sorted_students:
        print(f"{name} -> {average_grade:.2f}")