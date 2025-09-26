def calculate_average(grades):
    average = round(sum(grades) / len(grades))

    return average

def calculate_average_for_all_students(students_list):
    summ_of_avg = 0

    for student in students_list:
        summ_of_avg += calculate_average(student['grades'])

    result = round(summ_of_avg / len(students_list))

    return result


students = [
    {'name': 'John', 'grades': [80, 90, 78]},
    {'name': 'Michael', 'grades': [78, 75, 82]},
    {'name': 'Jenny', 'grades': [91, 83, 77]},
    {'name': 'Ken', 'grades': [60, 84, 66]},
    {'name': 'Sadoveg', 'grades': [65, 65, 65]},
]

avg_students_grades = [calculate_average(students[i]['grades']) for i in range(len(students))]


for i in range (len(students)):
    print(f'Студент: {students[i]["name"]}')

    print(f'Средний балл: {avg_students_grades[i]}')

    print(f'Статус: {'Успешен' if avg_students_grades[i] > 75 else 'Отстающий'}\n')

print(f'Общий средний балл по всем студентам: {calculate_average_for_all_students(students)}')

students.append({'name': 'Mihail', 'grades': [95, 94, 93]})

avg_students_grades.append(calculate_average(students[-1]['grades']))

print(f'Общий средний балл по всем студентам: {calculate_average_for_all_students(students)}')

students.pop(avg_students_grades.index((min(avg_students_grades))))

avg_students_grades.pop(avg_students_grades.index((min(avg_students_grades))))

print(f'Общий средний балл по всем студентам: {calculate_average_for_all_students(students)}')