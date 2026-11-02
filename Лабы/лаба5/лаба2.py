print("Введите N")
n = int(input())

if n < 1:
    print("N должно быть не меньше 1")
else:
    total = 0
    fact = 1
    sum_sq = 0

    for i in range(1, n + 1):
        total += i
        fact *= i
        sum_sq += i * i

    print(f'Сумма чисел от 1 до {n}: {total}')
    print(f'Произведение чисел от 1 до {n} (факториал): {fact}')
    print(f'Сумма квадратов чисел от 1 до {n}: {sum_sq}')
