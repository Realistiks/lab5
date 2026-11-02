print("Введите число")
n = int(input())

x = abs(n)

if x == 0:
    count, total, prod, rev = 1, 0, 1, 0
else:
    count = 0
    total = 0
    prod = 1
    rev = 0

    while x > 0:
        digit = x % 10
        count += 1
        total += digit
        prod *= digit
        rev = rev * 10 + digit
        x //= 10

if n < 0:
    rev = -rev

print(f"Количество цифр: {count}")
print(f"Сумма цифр: {total}")
print(f"Произведение цифр: {prod}")
print(f"Перевёрнутое число: {rev}")
