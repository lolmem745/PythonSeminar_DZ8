import logger


def save_student(student):
    with open('students.csv', 'a', encoding='utf-8') as file:
        file.write(f"{student['Id']},{student['First Name']},{student['Last Name']},{student['Birthday']}\n")
    logger.log('Student saved as Data.')


def save_all_students(students):
    with open('students.csv', 'w', encoding='utf-8') as file:
        file.write('Id;First Name;Last Name;Birthday\n')
        for item in students:
            file.write(
                f"{item},{students[item]['First Name']},{students[item]['Last Name']},{students[item]['Birthday']}")
    logger.log('Students saved as Data.')


def save_last_student_id(student_id_counter):
    with open('last_student_id.txt', 'w', encoding='utf-8') as file:
        file.write(str(student_id_counter))
    logger.log('Last student`s id saved.')


def save_grades(grades):
    with open('grades.txt', 'w', encoding='utf-8') as file:
        for key, value in grades.items():
            file.write(key + ' - [')
            file.write(str(value[0]))
            for i in range(1, len(value)):
                file.write(', ')
                file.write(str(value[i]))
            file.write(']\n')
    logger.log('Grades saved as Data.')
