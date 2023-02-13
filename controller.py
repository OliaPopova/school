import view


main_dict = {}
name_list = []
lesson_list = []


def start():
    while True:
        op = view.get_op()
        if op == 1:
            name = view.input_student()
            if name not in name_list:
                main_dict[name] = {}
                for lesson in lesson_list:
                    main_dict[name][lesson] = []

        if op == 2:
            lesson = view.input_lesson()
            if lesson not in lesson_list:
                lesson_list.append(lesson)
                for name in name_list:
                    main_dict[name][lesson] = []

        if op == 3:
            name, lesson, mark = view.add_mark()
            main_dict[name][lesson].append(mark)

        if op == 4:
            print(main_dict)

        if op == 5:
            name = view.input_student_info()
            print(main_dict[name])
        if op == 6:
            break

