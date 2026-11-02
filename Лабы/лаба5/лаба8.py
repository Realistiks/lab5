print("Перевод систем счисления")
print("1 - десятичное в двоичное")
print("2 - двоичное в десятичное")
choice = input("Ваш выбор: ")

if choice == "1":
    n = int(input("Десятичное число: "))
    sign = "-" if n < 0 else ""
    x = abs(n)
    bits = ""
    if x == 0:
        bits = "0"
    while x > 0:
        bits = str(x % 2) + bits
        x //= 2
    print("Двоичное число: " + sign + bits)

elif choice == "2":
    s = input("Двоичное число: ")
    sign = -1 if s[0] == "-" else 1
    digits = s.replace("-", "")
    value = 0
    correct = len(digits) > 0
    for c in digits:
        if c == "0" or c == "1":
            value = value * 2 + int(c)
        else:
            correct = False
    if correct:
        print("Десятичное число: " + str(sign * value))
    else:
        print("Ошибка: можно только 0 и 1")

else:
    print("Нет такого пункта меню")
