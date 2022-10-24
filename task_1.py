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

from collections import Counter
from timeit import timeit


def haffman_tree(string):
    tuple_list = Counter(string).most_common()
    sorted_vals = sorted(tuple_list, key=lambda val: val[1])
    if len(sorted_vals) != 1:
        while len(sorted_vals) > 1:
            node = sorted_vals[0][1] + sorted_vals[1][1]
            comb = {0: sorted_vals.pop(0)[0],
                    1: sorted_vals.pop(0)[0]}
            for n, count in enumerate(sorted_vals):
                if node > count[1]:
                    continue
                else:
                    sorted_vals.insert(n, (comb, node))
                    break
            else:
                sorted_vals.append((comb, node))
    else:
        node = sorted_vals[0][1]
        comb = {0: sorted_vals.pop(0)[0], 1: None}
        sorted_vals.append((comb, node))
    return sorted_vals[0][0]


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


txt = "Hello World!"
with open("text_.txt", "w") as fu:
    fu.write(txt)

code_table = {}
haffman_code(haffman_tree(txt))
# print(code_table)
code_table_tuple = list(code_table.items())
for i in range(len(code_table_tuple)):
    print(f'Кодировка Хаффмана {code_table_tuple[i][0]}: {code_table_tuple[i][1]}')
print()
print(timeit('haffman_code(haffman_tree(txt))', globals=globals(), number=1000))
