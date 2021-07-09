"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать программу, которая будет выводить количество четных и нечетных значений
в списке из целых чисел

even - четные
odd - нечетные
"""


def calc_even_odd(array: list) -> tuple:
    even = []
    odd = []
    for i in array:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return len(even), len(odd)


if __name__ == '__main__':
    assert calc_even_odd([2, 1, 5, 4, 7]) == (2, 3)
    print('Решено!')
