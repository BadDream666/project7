original_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(original_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, принимающая список словарей и выдает новый список с заданным ключом"""

    filtered_list: list[dict] = []

    for item in original_list:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list


# print(filter_by_state(original_list, "CANCELED"))
# print(filter_by_state(original_list, "EXECUTED"))

def sort_by_date(original_list: list[dict], reverse=True[dict]) -> list[dict]:
    """Функиця, сортирующая исходные данные по дате"""

    sorted_list: list[dict] = sorted(original_list, key=lambda inform_state: inform_state["date"],
                                     reverse=reverse[dict])
    return sorted_list

# print(sort_by_date(original_list, True))
