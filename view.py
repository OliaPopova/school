def get_op():
    op = int(input(
        " 1 - добавить ученика,\n 2 - добавить предмет,\n 3 - добавить оценку,\n 4 - показать весь список,"
        "\n 5 - показать конкретного ученика,\n 6 - выход\n"))
    return op


def input_student():
    name = input("Введите имя и фамилию нового ученика: ")
    return name


def input_lesson():
    lesson = input("Введите предмет: ")
    return lesson


def add_mark():
    name = input("Введите фамилию ученика: ")
    lesson = input("Введите предмет: ")
    mark = input("Введите оценку: ")
    return name, lesson, mark


def input_student_info():
    name = input("Введите имя и фамилию для просмотра оценок: ")
    return name
