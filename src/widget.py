import re
import masks

def mask_account_card(type_number: str) -> str:
    """Возвращает строку с замаскированным номером карты или счета"""
    list_numbers = re.findall(r'\d+', type_number)
    number = int(list_numbers[0])
    if len(list_numbers[0]) == 16:
        result = masks.get_mask_card_number(number)
    elif len(list_numbers[0]) == 20:
        result = masks.get_mask_account(number)
    else:
        result = "Проверьте корректность входных данных"
    return result

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Счет 784304305"))
