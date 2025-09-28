def calculate_average(grades):
    average = round(sum(grades) / len(grades))

    return average


def calculate_average_for_all_students(students_list):
    summ_of_avg = 0

    for student in students_list:
        summ_of_avg += calculate_average(student['grades'])

    result = round(summ_of_avg / len(students_list))

    print(f'Общий средний балл по всем студентам: {result}\n')


def add_student(student_dict):
    students.append(student_dict)

    avg_students_grades.append(calculate_average(students[-1]['grades']))

    calculate_average_for_all_students(students)


def delete_student_with_least_avg(students_list):
    students.pop(avg_students_grades.index((min(avg_students_grades))))

    avg_students_grades.pop(avg_students_grades.index((min(avg_students_grades))))

    calculate_average_for_all_students(students)


def print_journal(students_list):
    for i in range(len(students_list)):
        print(f'Студент: {students_list[i]["name"]}')

        print(f'Средний балл: {avg_students_grades[i]}')

        print(f'Статус: {'Успешен' if avg_students_grades[i] > 75 else 'Отстающий'}\n')


students = [
    {'name': 'John', 'grades': [80, 90, 78]},
    {'name': 'Michael', 'grades': [78, 75, 82]},
    {'name': 'Ken', 'grades': [60, 84, 66]},
    {'name': 'Sadoveg', 'grades': [65, 65, 65]},
]

avg_students_grades = [calculate_average(students[i]['grades']) for i in range(len(students))]

print_journal(students)

add_student({'name': 'Jenny', 'grades': [91, 83, 77]})

delete_student_with_least_avg(students)

print_journal(students)