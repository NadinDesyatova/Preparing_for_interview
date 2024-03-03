# Реализован класс Stack со следующими методами:
# is_empty — проверка стека на пустоту. Метод возвращает True или False;
# push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
# pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
# peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
# size — возвращает количество элементов в стеке.

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack:
            return False

        return True

    def push(self, new_element):
        self.stack.append(new_element)

    def pop(self):
        last_element_for_delete = self.stack.pop()

        return last_element_for_delete

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
