from time import sleep

from lab3.lab_python_fp.field import field
from lab3.lab_python_fp.gen_random import gen_random
from lab3.lab_python_fp.unique import Unique
from lab3.lab_python_fp.sort import sort
from lab3.lab_python_fp.print_result import print_result
from lab3.lab_python_fp.cm_timer1 import cm_timer1
from lab3.lab_python_fp.cm_timer2 import cm_timer2


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


def main():

    # task 1
    print('------------------------------------------task 1------------------------------------------\n')
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    field_gen = field(goods, 'title')
    for i in field_gen:
        print(i)
    field_gen = field(goods, 'title', 'price')
    for i in field_gen:
        print(i)

    # task 2
    print('------------------------------------------task 2------------------------------------------\n')
    random_gen = gen_random(5, 1, 3)
    for i in random_gen:
        print(i)

    # task 3
    print('------------------------------------------task 3------------------------------------------\n')
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    Unique(data).print_unique()
    data = gen_random(10, 1, 3)
    Unique(data).print_unique()
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    Unique(data).print_unique()
    Unique(data, ignore_case=True).print_unique()

    # task 4
    print('------------------------------------------task 4------------------------------------------\n')
    data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
    print(sort(data))

    # task 5
    print('------------------------------------------task 5------------------------------------------\n')
    test_1()
    test_2()
    test_3()
    test_4()

    # task 6
    print('------------------------------------------task 6------------------------------------------\n')
    with cm_timer1():
        sleep(2)
    with cm_timer2():
        sleep(2)

    # task 7
    print('------------------------------------------task 7------------------------------------------\n')


if __name__ == "__main__":
    main()
