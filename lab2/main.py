from lab2.lab_python_oop.rectangle import Rectangle
from lab2.lab_python_oop.circle import Circle
from lab2.lab_python_oop.square import Square


def main():
    r = Rectangle("синий", 3, 2)
    c = Circle("зеленый", 5)
    s = Square("красный", 5)
    print(r)
    print(c)
    print(s)


if __name__ == '__main__':
    main()
