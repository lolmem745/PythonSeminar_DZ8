import view
import logger
import get_data
import save_data


def add_new_student(student_id_counter):
    new_student = dict()
    new_student['Id'] = get_data.get_new_id(student_id_counter)
    new_student['First Name'] = view.get_new_student_info('student`s first name')
    new_student['Last Name'] = view.get_new_student_info('student`s last name')
    new_student['Birthday'] = view.get_new_student_info('student`s birthday')
    logger.log('Student successfully added.')
    add_students_in_grades(new_student['Id'])
    return new_student


def add_students_in_grades(student_id):
    grades = get_data.get_grades()
    student_grade = view.get_new_student_info('student`s grade')
    if student_grade in grades:
        grades[student_grade].append(student_id)
        logger.log('New grade successfully created.')
    else:
        grades[student_grade] = [student_id]
    logger.log('Student successfully added in grade.')
    save_data.save_grades(grades)


def delete_student():
    grades = get_data.get_grades()
    student_id = view.get_new_student_info(
        'student`s id you want to expel.\nIf you want to check all students press "look"')
    students = get_data.get_all_students()
    temp = []

    if student_id.lower() == 'look':
        view.print_all_students(students)
        student_id = view.get_new_student_info('student`s id you want to expel: ')

    for gr in grades:
        if student_id in grades[gr]:
            grades[gr].remove(student_id)
            if grades[gr] == []:
                temp.append(gr)
            logger.log('Student removed from the grade.')
        else: view.error()

    for element in temp:
        grades.pop(element)
        logger.log('Grade removed. No students in grade.')

    students.pop(student_id, None)
    save_data.save_all_students(students)
    logger.log('Student expeled.')
    save_data.save_grades(grades)


def info_change():
    students = get_data.get_all_students()
    student_id = view.get_new_student_info(
        'student`s id you want to rename.\nIf you want to check all students press "look"')

    if student_id.lower() == 'look':
        view.print_all_students(students)
        student_id = view.get_new_student_info('student`s id you want to rename: ')

    students[student_id]['First Name'] = view.get_new_student_info('student`s first name')
    students[student_id]['Last Name'] = view.get_new_student_info('student`s last name')
    students[student_id]['Birthday'] = view.get_new_student_info('student`s birthday') + '\n'
    logger.log('Student successfully renamed.')
    save_data.save_all_students(students)


def student_transfer():
    grades = get_data.get_grades()
    student_id = view.get_new_student_info(
        'student`s id you want to transfer to another grade.\nIf you want to check all students press "look"')
    students = get_data.get_all_students()
    temp = []

    if student_id.lower() == 'look':
        view.print_all_students(students)
        student_id = view.get_new_student_info('student`s id you want to transfer to another grade: ')

    for gr in grades:
        if student_id in grades[gr]:
            grades[gr].remove(student_id)
            if grades[gr] == []:
                temp.append(gr)
            logger.log('Student removed from the grade.')

    for element in temp:
        grades.pop(element)
        logger.log('Grade removed. No students in grade.')

    save_data.save_grades(grades)
    add_students_in_grades(student_id)
    logger.log('Student transfered.')
