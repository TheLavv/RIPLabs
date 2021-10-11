def sort(data):
    return [sorted(data, reverse=True, key=abs), sorted(data, reverse=True, key=lambda x: -x if (x < 0) else x)]
