def process_argument(argument):
    if isinstance(argument, dict):
        # Если аргумент - словарь, найдем ключ с максимальным значением
        if argument:
            max_key = max(argument, key=argument.get)
            print(f"Ключ с максимальным значением: {max_key}")
        else:
            print("Пустой словарь")
    elif isinstance(argument, list):
        # Если аргумент - список, найдем количество элементов до первого отрицательного элемента
        count = 0
        for elem in argument:
            if elem < 0:
                break
            count += 1
        print(f"Количество элементов до первого отрицательного элемента: {count}")
    elif isinstance(argument, int):
        # Если аргумент - число, проверим, является ли оно простым
        if argument > 1:
            for i in range(2, argument):
                if (argument % i) == 0:
                    print(f"{argument} не является простым числом")
                    break
            else:
                print(f"{argument} является простым числом")
        else:
            print("Число должно быть больше 1")
    elif isinstance(argument, str):
        # Если аргумент - строка, выведем ее в обратном порядке и найдем сумму цифр
        reversed_str = argument[::-1]
        print(f"Строка в обратном порядке: {reversed_str}")
        digits_sum = sum(int(digit) for digit in argument if digit.isdigit())
        print(f"Сумма цифр в строке: {digits_sum}")
    else:
        print("Неизвестный тип аргумента")

# Примеры вызова функции:
process_argument({'a': 10, 'b': 20, 'c': 5})  # Вывод ключа с максимальным значением
process_argument([1, 2, 3, -1, 4, 5])       # Вывод количества элементов до первого отрицательного
process_argument(17)                        # Проверка на простоту
process_argument("Hello12345")