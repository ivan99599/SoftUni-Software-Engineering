exam_results = {}

while True:
    command = input()
    if command == "exam finished":
        break
    username, language, points = command.split("-")
    current_points = int(points)
    if username not in exam_results:
        exam_results[username] = []
    exam_results[username].append(language)
    if current_points > exam_results.values()
        exam_results[username].append(current_points)




