def calculate_average(grades):
        average = round(sum(grades) / len(grades))

        return average


def calculate_average_for_all_students(students_list):
    if len(students_list) != 0:
        summ_of_avg = 0

        for student in students_list:
            summ_of_avg += calculate_average(student['grades'])

        result = round(summ_of_avg / len(students_list))

        print(f'Общий средний балл по всем студентам: {result}\n')
    else:
        print('Список студентов пуст!')


def add_student(students_list, student_dict, avgs_list):
    students_list.append(student_dict)

    avgs_list.append(student_dict['grades'])

    calculate_average_for_all_students(students_list)

    return students_list, avgs_list


def delete_student_with_least_avg(students_list, avgs_list):
    if len(students_list) != 0:
        min_index = avg_students_grades.index((min(avg_students_grades)))

        students_list.pop(min_index)

        avgs_list.pop(min_index)

        calculate_average_for_all_students(students_list)

        return students_list, avgs_list

    print('Список студентов уже пуст!\n')


def print_journal(students_list):
    for i in range(len(students_list)):
        print(f'Студент: {students_list[i]["name"]}\nСредний балл: {avg_students_grades[i]}')

        print(f'Статус: {'Успешен' if avg_students_grades[i] > 75 else 'Отстающий'}\n')


students = [
    {'name': 'John', 'grades': [80, 90, 78]},
    {'name': 'Michael', 'grades': [78, 75, 82]},
    {'name': 'Ken', 'grades': [60, 84, 66]},
    {'name': 'Sadoveg', 'grades': [65, 65, 65]},
]

avg_students_grades = [calculate_average(students[i]['grades']) for i in range(len(students))]

print_journal(students)

calculate_average_for_all_students(students)

students, avg_students_grades = add_student(students, {'name': 'Jenny', 'grades': [91, 83, 77]}, avg_students_grades)

students, avg_students_grades = delete_student_with_least_avg(students, avg_students_grades)

print_journal(students)