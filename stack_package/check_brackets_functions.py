from stack_package.stack import Stack


def define_close_bracket(open_bracket):
    close_bracket: str = ''
    if open_bracket == '(':
        close_bracket = ')'
    elif open_bracket == '{':
        close_bracket = '}'
    elif open_bracket == '[':
        close_bracket = ']'

    return close_bracket


def define_open_bracket(close_bracket):
    open_bracket: str = ''
    if close_bracket == ')':
        open_bracket = '('
    elif close_bracket == '}':
        open_bracket = '{'
    elif close_bracket == ']':
        open_bracket = '['

    return open_bracket


def create_bracket_dict(brackets_string):
    exist_brackets: dict = {}
    for index, bracket in enumerate(brackets_string):
        if bracket not in exist_brackets:
            exist_brackets[bracket] = []
            exist_brackets[bracket].append(index)

        elif bracket in exist_brackets:
            exist_brackets[bracket].append(index)

    return exist_brackets


def check_brackets_number(brackets_string, brackets_dict):
    number_stack: Stack = Stack()
    for bracket in brackets_dict:
        if bracket in ['(', '{', '[']:
            open_bracket_number = brackets_string.count(bracket)
            close_bracket = define_close_bracket(bracket)
            close_bracket_number = brackets_string.count(close_bracket)
            number_stack.push({
                'open_bracket': open_bracket_number,
                'close_bracket': close_bracket_number
            })

        else:
            open_bracket = define_open_bracket(bracket)
            if open_bracket not in brackets_string:
                return 'Не равно'

    while not number_stack.is_empty():
        last_item = number_stack.peek()
        if last_item['open_bracket'] == last_item['close_bracket']:
            number_stack.pop()
        else:
            return 'Не равно'


def check_correct_nesting(exist_brackets):
    new_stack: Stack = Stack()
    for bracket, value in exist_brackets.items():
        if bracket in ['(', '[', '{']:
            new_stack.push({bracket: value})
            close_bracket = define_close_bracket(bracket)
            bracket_indexes: list = new_stack.peek()[bracket]
            number_indexes = len(bracket_indexes)
            checked_indexes: list = []
            for bracket, value in exist_brackets.items():
                if bracket == close_bracket:
                    for i in range(number_indexes):
                        for index_close_bracket in value:
                            if index_close_bracket not in checked_indexes:
                                index_open_bracket = bracket_indexes[-1]
                                if index_close_bracket > index_open_bracket:
                                    difference = index_close_bracket - index_open_bracket
                                    if difference % 2 == 1:
                                        checked_indexes.append(index_close_bracket)
                                        bracket_indexes.pop()
                                    else:
                                        return 'Неправильно'
                                else:
                                    continue

            if bracket_indexes:
                return 'Неправильно'

            new_stack.pop()

    if new_stack.is_empty():
        return 'Правильно'
