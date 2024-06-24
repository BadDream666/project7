import src.masks


def mask_account_card(card_number: str) -> str:
    """Функция, максирующая счета и карты"""
    if "Счет" in card_number:
        return src.masks.get_mask_account(card_number)
    else:
        cards = src.masks.get_mask_card_number(card_number[-16:])
        new_card = card_number.replace(card_number[-16:], cards)
        return new_card


def get_data(data: str) -> str:
    """Функция, преобразующая формат даны"""
    return f"{data[8:10]}.{data[5:7]}.{data[0:4]}"
