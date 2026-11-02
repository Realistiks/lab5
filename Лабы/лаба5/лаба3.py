print("Сколько чисел Фибоначчи вывести?")
n = int(input())

if n < 1:
    print("Введите положительное число")
else:
    a, b = 0, 1
    row = []
    for _ in range(n):
        row.append(a)
        a, b = b, a + b

    print(f"Первые {n} чисел Фибоначчи:")
    print(" ".join(str(x) for x in row))
