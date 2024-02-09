students = []
course_to_search = None
while True:
    command = input()
    if ":" not in command:
        course_to_search = command
        break
    name, student_id, course = command.split(":")
    students.append({"name": name, "ID": student_id, "course": course })

for student in students:
    if course_to_search.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['ID']}")

