def swap_max_and_min(a) -> list:
    set_list = set(a)
    if len(list(set_list)) == len(a):
        try:
            min_ind = a.index(min(a))
            max_ind = a.index(max(a))
            a[max_ind], a[min_ind] = a[min_ind], a[max_ind]
            return a
        except TypeError:
           raise TypeError
    else:
        raise ValueError
