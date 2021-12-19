import json
from lab3.lab_python_fp.cm_timer1 import cm_timer1
from lab3.lab_python_fp.print_result import print_result
from lab3.lab_python_fp.unique import Unique
from lab3.lab_python_fp.gen_random import gen_random

path = r"D:\home\RIPLabs\lab3\data_light.json"

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(data):
    return sorted(Unique((data[x]["job-name"] for x, _ in enumerate(data)), ignoreCase=True), key=lambda x: x.lower())


@print_result
def f2(data):
    return list(filter(lambda x: x.startswith('программист'), data))


@print_result
def f3(data):
    return list(map(lambda x: x + " с опытом Python", data))


@print_result
def f4(data):
    sal_gen = gen_random(len(data), 100000, 200000)
    return list(zip(data, sal_gen))


if __name__ == '__main__':
    with cm_timer1():
        f4(f3(f2(f1(data))))
