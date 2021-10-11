class Unique(object):
    def __init__(self, items, **kwargs):
        self.elements = {}
        ignore_case = kwargs.get('ignore_case')

        if ignore_case is None:
            ignore_case = False
        elif not isinstance(ignore_case, bool):
            raise Exception(
                "ignore_case parameter is not Boolean")

        for item in items:
            if ignore_case is True and isinstance(item, str):
                item = item.lower()

            self.elements[item] = item

    def __next__(self):
        return next(self.elements)

    def __iter__(self):
        return iter(self.elements)

    def print_unique(self):
        print("[", end="")
        print(*self.elements, sep=", ", end="")
        print("]")
