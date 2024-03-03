from stack_package.check_brackets_functions import create_bracket_dict, check_brackets_number, check_correct_nesting


def check_brackets(brackets_string):
    if not brackets_string:
        return 'Передана пустая строка'

    exist_brackets = create_bracket_dict(brackets_string)

    number = check_brackets_number(brackets_string, exist_brackets)
    if number == 'Не равно':
        return 'Несбалансированно'

    nesting = check_correct_nesting(exist_brackets)
    if nesting == 'Неправильно':
        return 'Несбалансированно'

    return 'Сбалансированно'
