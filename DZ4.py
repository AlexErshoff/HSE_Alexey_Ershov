def validate_inn(inn: str) -> bool:
    """
    Проверяет валидность ИНН (для организаций и физ. лиц/ИП)

    :param inn: строка с ИНН (10 или 12 цифр)
    :return: True если ИНН валиден, False если нет
    """
    # Преобразуем в строку и очищаем от возможных пробелов
    inn = str(inn).strip()

    # Проверка базовых условий
    if not inn.isdigit():
        return False

    if len(inn) == 10:
        return _validate_org_inn(inn)
    elif len(inn) == 12:
        return _validate_person_inn(inn)
    else:
        return False


def _validate_org_inn(inn: str) -> bool:
    """Проверка ИНН организации (10 цифр)"""
    if len(inn) != 10 or not inn.isdigit():
        return False

    # Коэффициенты для проверки
    coefficients = [2, 4, 10, 3, 5, 9, 4, 6, 8]

    # Вычисляем контрольную сумму
    control_sum = sum(int(inn[i]) * coefficients[i] for i in range(9))

    # Вычисляем контрольное число
    control_number = control_sum % 11
    if control_number > 9:
        control_number = control_number % 10

    # Сравниваем с последней цифрой ИНН
    return control_number == int(inn[9])


def _validate_person_inn(inn: str) -> bool:
    """Проверка ИНН физ. лица/ИП (12 цифр)"""
    if len(inn) != 12 or not inn.isdigit():
        return False

    # Проверяем первое контрольное число
    coefficients_1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    control_sum_1 = sum(int(inn[i]) * coefficients_1[i] for i in range(10))

    control_number_1 = control_sum_1 % 11
    if control_number_1 > 9:
        control_number_1 = control_number_1 % 10

    if control_number_1 != int(inn[10]):
        return False

    # Проверяем второе контрольное число
    coefficients_2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    control_sum_2 = sum(int(inn[i]) * coefficients_2[i] for i in range(11))

    control_number_2 = control_sum_2 % 11
    if control_number_2 > 9:
        control_number_2 = control_number_2 % 10

    return control_number_2 == int(inn[11]))


    # Примеры использования
    if __name__ == "__main__":
    # Тестовые ИНН (варианты)
        test_inns = [
    "500100732259",  # Валидный ИНН физ. лица
    "7728168911",  # Валидный ИНН организации
    "1234567890",  # Невалидный ИНН
    "123456789012",  # Невалидный ИНН
    "abcdefghij",  # Не числа
    "123",  # Неправильная длина

]

for inn in test_inns:
    result = validate_inn(inn)
print(f"ИНН {inn}: {'валиден' if result else 'не валиден'}")