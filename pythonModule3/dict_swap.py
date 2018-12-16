
def dict_swap(dict) -> dict:
    try:
        dict_sw = {y: x for x, y in dict.items()}
        return dict_sw
    except TypeError:
        raise TypeError
