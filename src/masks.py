def get_mask_card_number(card_number: str) -> str:
    """Returns masked card number as string"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return card_number


def get_mask_account(acc_number: str) -> str:
    """Returns masked account number as string"""
    if acc_number.isdigit() and len(acc_number) == 20:
        return f"**{acc_number[-4::]}"
    else:
        return acc_number
