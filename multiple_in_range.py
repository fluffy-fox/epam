
def multiple_in_range(x, y):
    try:
        numbers = [i for i in range(x, y + 1) if i % 7 == 0 and i % 5 != 0]
        return numbers
    except TypeError:
        raise TypeError



