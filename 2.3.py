def create_chessboard(n, m):
    chessboard = []  # Создаем пустой массив
    for i in range(n):
        row = []  # Создаем пустую строку для каждой строки в массиве
        for j in range(m):
            # Заполняем ячейки массива символами "." и "*" в шахматном порядке
            if (i + j) % 2 == 0:
                row.append(".")
            else:
                row.append("*")
        chessboard.append(row)  # Добавляем строку к массиву
    return chessboard

# Пример использования функции:
n = 5  # Количество строк
m = 5  # Количество столбцов
board = create_chessboard(n, m)

# Выводим созданную шахматную доску
for row in board:
    print(" ".join(row))