def field(items, *args):
    assert len(args) > 0, 'at least one argument was expected'
    result = []

    for item in items:
        temp = {}
        for arg in args:
            value = item.get(arg)
            if value is not None:
                temp.update({arg: value})
        if temp:
            if len(args) == 1:
                yield temp[args[0]]
            else:
                yield temp
