def grade(current_grade):
    if 2 <= current_grade <= 2.99:
        return "Fail"
    elif 3 <= current_grade <= 3.49:
        return "Poor"
    elif 3.5 <= current_grade <= 4.49:
        return "Good"
    elif 4.5 <= current_grade <= 5.49:
        return "Very Good"
    elif 5.5 <= current_grade <= 6:
        return "Exellent"


current_grade = float(input())
result = grade(current_grade)
print(result)
