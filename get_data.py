import logger


def get_last_student_id():
    with open('last_student_id.txt', 'r', encoding='utf-8') as file:
        logger.log('Last student`s id successfully copied.')
        return int(file.read())


def get_new_id(student_id_counter):
    return student_id_counter + 1


def get_grades():
    grades = dict()

    with open('grades.txt', 'r', encoding='utf-8') as file:
        temp = file.readlines()

        for element in temp:
            grades[element[:element.index(' ')]] = element[element.index('[') + 1:-2].split(', ')
    logger.log('Grades successfully copied.')
    return grades


def get_all_students():
    students = dict()

    with open('students.csv', 'r', encoding='utf-8') as file:
        temp = file.readlines()
        temp.pop(0)
        # print(temp)
        # print()
        # student_info = dict()
    for element in temp:
        element = element.split(',')
        # print(element)
        # student_info['First Name'] = element.split(',')[1]
        # student_info['Last Name'] = element.split(',')[2]
        # student_info['Birthday'] = element.split(',')[3]
        students[element[0]] = {'First Name': element[1], 'Last Name': element[2], 'Birthday': element[3]}
    logger.log('All students copied.')
    return students
