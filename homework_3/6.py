def percentage_to_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'E'

percentages = [95, 85, 75, 65, 55]
for percentage in percentages:
    grade = percentage_to_grade(percentage)
    print(percentage,"->",grade)
