print("break: ищем первое чётное число")
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print("Первое чётное:", num)
        break

print()
print("continue: сумма только положительных чисел")
values = [5, -3, 8, -1, 10, -7, 2]
total = 0
for v in values:
    if v < 0:
        continue
    total += v
print("Сумма положительных:", total)

print()
print("pass: заглушка в теле цикла")
i = 1
while i <= 3:
    pass
    print("Итерация", i)
    i += 1
