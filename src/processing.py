def filter_by_state(sorting_list: list, key='EXECUTED') -> list:
    """Сортировка списка словарей по ключу state"""
    sorted_list = []
    for s in sorting_list:
        if s['state'] == key:
            sorted_list.append(s)
    return sorted_list


def sort_by_date(sorting_list: list, route=True) -> list:
    """Сортировка списка словарей по дате"""
    sorted_list = sorted(sorting_list, key=lambda s: s['date'], reverse=route)
    return sorted_list
