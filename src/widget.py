import src.masks


def mask_account_card(card_number: str) -> str:
    if "Счет" in card_number:
        return src.masks.get_mask_account(card_number)
    else:
        cards = src.masks.get_mask_card_number(card_number[-16:])
        new_card = card_number.replace(card_number[-16:], cards)
        return new_card


#print(mask_account_card("MasterCard 7158300734726758"))

def get_data(data: str) -> str:
    return f"{data[8:10]}.{data[5:7]}.{data[0:4]}"

#print(get_data("2018-07-11T02:26:18.671407"))
