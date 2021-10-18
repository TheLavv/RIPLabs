from operator import itemgetter


class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Browser:
    def __init__(self, id, name, memory_on_disk, comp_id):
        self.id = id
        self.name = name
        self.memory_on_disk = memory_on_disk
        self.comp_id = comp_id


class CompBrowser:
    def __init__(self, comp_id, browser_id):
        self.comp_id = comp_id
        self.browser_id = browser_id


# Компьютеры
computers = [
    Computer(1, 'Ноутбук ASUS A540L'),
    Computer(2, 'Компьютер HYPERPC NANO X'),
    Computer(3, 'Компьютер HYPERPC VOLT'),
    Computer(4, 'Ноутбук ASUS A540NV'),
    Computer(5, 'Компьютер ASUS A8'),
    Computer(6, 'Ноутбук ASUS A9'),
]

# Браузеры
browsers = [
    Browser(1, 'Google Chrome', 350, 1),
    Browser(2, 'Яндекс.Браузер', 250, 2),
    Browser(3, 'Mozilla Firefox', 400, 3),
    Browser(4, 'Opera', 300, 3),
    Browser(5, 'Safari', 280, 3),
]

comps_browsers = [
    CompBrowser(1, 1),
    CompBrowser(2, 2),
    CompBrowser(3, 3),
    CompBrowser(3, 4),
    CompBrowser(3, 5),
    CompBrowser(4, 1),
    CompBrowser(5, 2),
    CompBrowser(6, 3),
    CompBrowser(6, 4),
    CompBrowser(6, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(b.name, b.memory_on_disk, c.name)
                   for c in computers
                   for b in browsers
                   if b.comp_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, cb.comp_id, cb.browser_id)
                         for c in computers
                         for cb in comps_browsers
                         if c.id == cb.comp_id]

    many_to_many = [(b.name, b.memory_on_disk, comp_name)
                    for comp_name, _, browser_id in many_to_many_temp
                    for b in browsers if b.id == browser_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []

    # Перебираем все компьютеры
    for c in computers:
        c_browsers = list(filter(lambda i: i[2] == c.name, one_to_many))

        if len(c_browsers) > 0:
            c_memory_on_disk = [memory_on_disk for _, memory_on_disk, _ in c_browsers]
            c_memory_on_disk_sum = sum(c_memory_on_disk)
            res_12_unsorted.append((c.name, c_memory_on_disk_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все браузеры
    for c in computers:
        if 'Компьютер' in c.name:
            c_browsers = list(filter(lambda i: i[2] == c.name, many_to_many))
            c_browsers_names = [x for x, _, _ in c_browsers]
            res_13[c.name] = c_browsers_names

    print(res_13)


if __name__ == '__main__':
    main()
