import logger
import get_data


def export_students(students):
    file = open('students.csv', 'w', encoding='utf-8')
    file.write('Id,First Name,Last Name,Birthday\n')
    for key in students:
        file.write(f"{key},{students[key]['First Name']},{students[key]['Last Name']},{students[key]['Birthday']}")
    file.close()
    logger.log('students.csv created.')


def export_grades():
    grades = get_data.get_grades()
    students = dict()
    students = get_data.get_all_students()

    file = open('grades.csv', 'w', encoding='utf-8')
    file.write('Grade,Students\n')

    for key, value in grades.items():
        file.write(f'{key},')
        temp = []
        for id in students:
            if id in value:
                temp.append(students[id]['First Name'] + ' ' + students[id]['Last Name'])
        file.write(f"{', '.join(temp)}\n")

    file.close()
    logger.log('grades.csv created.')
