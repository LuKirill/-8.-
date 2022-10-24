"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def get_root_val(self):
        return self.root


class Error_root(Exception):
    "Значение узла не может быть больше значения корня в бинарном дереве"


try:
    r = BinaryTree(8)
    print(f'Корень {r.get_root_val()}')
    r.insert_left(4)
    print(f'Левый потомок {r.get_left_child().get_root_val()}')
    r.insert_right(25)
    print(f'Правый потомок {r.get_right_child().get_root_val()}')
    if r.get_root_val() < r.get_left_child().get_root_val():
        raise Error_root()
    if r.get_root_val() < r.get_right_child().get_root_val():
        raise Error_root()
except Error_root:
    print(f"Значение потомка не может быть больше значения родителя в бинарном дереве")
