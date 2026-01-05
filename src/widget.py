import re

def get_number(type_number: str) -> int:
    """Очистка номера счета/карты"""
    list_numbers = re.findall(r'\d+', type_number)
    number = int(list_numbers[0])
    return number


def mask_account_card(type_number: str) -> str:
    """Возвращает строку с замаскированным номером карты или счета"""
    pass
    return something

print(get_number("Visa Platinum 7000792289606361"))
print(get_number("Maestro 7000792289606361"))
print(get_number("Счет 73654108430135874305"))
