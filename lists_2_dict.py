def lists_2_dict(list1, list2) -> dict:
    try:
        dict_eq = dict(zip(list1, list2))
        return dict_eq
    except TypeError:
        raise TypeError
