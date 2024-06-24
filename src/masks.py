def get_mask_card_number(card_number: str) -> str | None:
    """Returns masked card number as string"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return None


# print(get_mask_card_number("7158300734726758"))


def get_mask_account(acc_number: str) -> str | None:
    """Returns masked account number as string"""
    if acc_number.isdigit() and len(acc_number) == 20:
        return f"**{acc_number[-4::]}"
    else:
        return None


# print(get_mask_account("73654108430135874305"))
