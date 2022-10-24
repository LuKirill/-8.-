"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
from timeit import timeit


def findTheCharFrequency(text):
    result = dict()
    with open(text, 'r') as f:
        for line in f.readlines():
            for i in line:
                if i in result:
                    result[i] += 1
                else:
                    result.update({i: 1})
    return result


class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None
        self.rchild = None


class HuffmanTree(object):
    def __init__(self, char_Weights):
        self.Leaf = [Node(k, v) for k, v in char_Weights.items()]
        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda node: node.value, reverse=True)
            n = Node(value=(self.Leaf[-1].value + self.Leaf[-2].value))
            n.lchild = self.Leaf.pop(-1)
            n.rchild = self.Leaf.pop(-1)
            self.Leaf.append(n)
        self.root = self.Leaf[0]
        self.Buffer = list(range(10))

    def Hu_generate(self, tree, length):
        node = tree
        if not node:
            return
        elif node.name:
            print(f'Кодировка Хаффмана {node.name}:', end=" ")
            for i in range(length):
                print(self.Buffer[i], end='')
            print()
            return
        self.Buffer[length] = 0
        self.Hu_generate(node.lchild, length + 1)
        self.Buffer[length] = 1
        self.Hu_generate(node.rchild, length + 1)

    def get_code(self):
        self.Hu_generate(self.root, 0)


txt = "Hello World!"
with open("text.txt", "w") as fu:
    fu.write(txt)
result = findTheCharFrequency('text.txt')
# print(result)
tree = HuffmanTree(result)
tree.get_code()
print()
print(timeit('findTheCharFrequency("text.txt")', globals=globals(), number=1000))
print(timeit('HuffmanTree(result)', globals=globals(), number=1000))

"""
Вариант с функцией отработал быстрей, чем с вариант с классами
вариант с функцией: 0.029250600025989115
вариант с классами: 0.11047650000546128+0.02321519999532029

Для удобства сделал одинаковый ввод и вывод данных.
В task_1 изменил названия переменных, убрал метод deque, добавил чтение из файла, изменил вывод данных
"""