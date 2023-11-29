try:
    # Попытка выполнения кода, который может вызвать исключение
    num = int(input("Введите число: "))
    result = 10 / num  # Если num будет 0, то это вызовет исключение ZeroDivisionError

except ZeroDivisionError:
    print("Ошибка деления на ноль.")
except ValueError:
    print("Ошибка ввода. Введите целое число.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Блок finally выполняется всегда, независимо от наличия исключений
    print("Блок finally всегда выполняется.")

print("Программа завершена.")