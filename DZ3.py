# 1. Математические функции

def factorial(n: int) -> int:
    """Вычисление факториала числа"""
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def max_of_three(numbers: tuple) -> float:
    """Поиск наибольшего из трех чисел"""
    if len(numbers) != 3:
        raise ValueError("Функция принимает кортеж из ровно трех чисел")
    return max(numbers)


def right_triangle_area(a: float, b: float) -> float:
    """Расчет площади прямоугольного треугольника"""
    return 0.5 * a * b


# 2. Функции для генерации текста с адресом суда

# Данные арбитражных судов (обычно это бы в отдельном файле)
ARBITRATION_COURTS = {
    "A40": {
        "name": "Арбитражный суд города Москвы",
        "address": "115225, г. Москва, ул. Б. Тульская, 17"
    },
    "A41": {
        "name": "Арбитражный суд Московской области",
        "address": "143407, Московская обл., г. Красногорск, бульвар Строителей, д. 4"
    },
    # Можно добавить другие суды по мере необходимости
}


def generate_court_header(respondent_data: dict, case_number: str) -> str:
    """
    Генерация шапки процессуального документа с реквизитами сторон

    :param respondent_data: словарь с данными ответчика
    :param case_number: номер дела
    :return: строка с готовой шапкой
    """
    # Получаем код суда из номера дела (первые символы до дефиса)
    court_code = case_number.split("-")[0]

    # Получаем данные суда
    court = ARBITRATION_COURTS.get(court_code, {
        "name": "Арбитражный суд",
        "address": "Адрес не указан"
    })

    # Данные истца (мои данные)
    plaintiff = {
        "name": "Иванов Иван Иванович",
        "inn": "123456789012",
        "ogrn": "123456789012345",
        "address": "123456, г. Москва, ул. Примерная, д. 1, кв. 2"
    }

    # Генерация шапки с помощью f-strings
    header = f"""В {court['name']}
Адрес: {court['address']}

Истец: {plaintiff['name']}
ИНН {plaintiff['inn']} ОГРНИП {plaintiff['ogrn']}
Адрес: {plaintiff['address']}

Ответчик: {respondent_data.get('name', 'Название не указано')}
ИНН {respondent_data.get('inn', 'не указан')} ОГРН {respondent_data.get('ogrn', 'не указан')}
Адрес: {respondent_data.get('address', 'не указан')}

Номер дела {case_number}
"""

    return header


def generate_all_court_headers(respondents_list: list) -> None:
    """
    Генерация шапок для всех ответчиков в списке

    :param respondents_list: список словарей с данными ответчиков
    """
    for i, respondent in enumerate(respondents_list, 1):
        case_number = respondent.get('case_number', f"A40-000000/{2023 + i}")
        print(f"=== Документ {i} ===")
        print(generate_court_header(respondent, case_number))
        print("\n")


# Пример использования
if __name__ == "__main__":
    # Пример данных ответчиков
    respondents_data = [
        {
            "name": "ООО 'Кооператив Озеро'",
            "inn": "1231231231",
            "ogrn": "123124129312941",
            "address": "123534, г. Москва, ул. Красивых молдавских партизан, 69",
            "case_number": "A40-123456/2023"
        },
        {
            "name": "ЗАО 'СтройГарант'",
            "inn": "9876543210",
            "ogrn": "987654321098765",
            "address": "117534, г. Москва, Ленинский проспект, 158",
            "case_number": "A41-654321/2023"
        },
        {
            "name": "ИП Сидоров П.П.",
            "inn": "5678901234",
            "ogrn": "567890123456789",
            "address": "109456, г. Москва, ул. Садовая, 15",
            "case_number": "A40-987654/2023"
        }
    ]

    # Генерация всех шапок
    generate_all_court_headers(respondents_data)

    # Примеры математических вычислений
    print(f"Факториал 5: {factorial(5)}")
    print(f"Максимальное из (3, 5, 2): {max_of_three((3, 5, 2))}")
    print(f"Площадь треугольника с катетами 3 и 4: {right_triangle_area(3, 4)}")

    # 1	- функция вычисления факториала числа (произведение натуральных чисел от 1 до n). Принимает в качестве аргумента число, возвращает его факториал

    n = int(input("Введите любое число: "))


    def factorial(n):
        if int(n) < 1:
            return 1
        else:
            return int(n) * factorial(n - 1)


    result = factorial(n)
    print("Факториал числа", n, "(", n, "!", ")", "равен", result)

    # - поиск наибольшего числа из трёх. Принимает в качестве аргумента кортеж из трёх чисел, возвращает наибольшее из них;

    tup = 100, 700, 104
    largest = max(tup)
    print("Самое большое число: ", largest)

    # - расчёт площади прямоугольного треугольника. Принимает в качестве аргумента размер двух катетов треугольника.
    # Возвращает площадь треугольника

    ab = int(input("Определим площадь прямоугольного треугольника ABC. Введите размер катета AB в сантиметрах: "))
    bc = int(input("Введите размер катета BC: в сантиметрах "))
    S = ab * bc // 2
    print("Площадь данного прямоугольного треугольника равна:", S, "см")

    # 2.	Создайте функцию для генерации текста с адресом суда.
    # Функция должна по шаблону генерировать шапку для процессуальных документов с реквизитами сторон для отправки.

    import json

    # Загрузка данных из файла
    with open('lesson_2_data.py', 'r', encoding='utf-8') as file:
        courts_data = json.load(file)


    def generate_court_address(defendant_data, case_number):
        """Генерирует шапку для процессуальных документов."""
        # Извлечение кода суда из номера дела
        court_code = case_number.split('-')[0]

        # Поиск данных суда по коду
        court_info = next((court for court in courts_data if court['code'] == court_code), None)
        if not court_info:
            return "Суд не найден."

        # Шаблон для заполнения
        template = f"""
    В арбитражный суд {court_info['name']}
    Адрес: {court_info['address']}

    Истец: Архипов Алексей Владимирович
    ИНН 1236182357 ОГРНИП 218431927812733
    Адрес: 123534, г. Москва, ул. Водников, 13

    Ответчик: {defendant_data['name']}
    ИНН {defendant_data['inn']} ОГРН {defendant_data['ogrn']}
    Адрес: {defendant_data['address']}

    Номер дела {case_number}
    """
        return template.strip()


    # Пример использования:
    defendant_data = {
        "name": "ООО “Кооператив Озеро”",
        "inn": "1231231231",
        "ogrn": "123124129312941",
        "address": "123534, г. Москва, ул. Красивых молдавских партизан, 69"
    }
    case_number = "А40-123456/2023"

    print(generate_court_address(defendant_data, case_number))
