def filter_by_state(sorting_list: list, key = 'EXECUTED') -> list:
    """Сортировка списка словарей по ключу state"""
    sorted_list = []
    for s in sorting_list:
        if s['state'] == key:
            sorted_list.append(s)
    return sorted_list
