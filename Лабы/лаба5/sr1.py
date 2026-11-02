import random

digits = random.sample("0123456789", 4)
while digits[0] == "0":
    digits = random.sample("0123456789", 4)
number = "".join(digits)

print("Быки и коровы")
print("Загадано 4-значное число, попробуйте угадать")

tries = 0
while True:
    guess = input("Ваш вариант: ")
    if len(guess) != 4 or not guess.isdigit() or guess[0] == "0":
        print("Нужно ввести 4 цифры, первая не ноль")
        continue

    tries += 1
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == number[i]:
            bulls += 1
        elif guess[i] in number:
            cows += 1

    if bulls == 4:
        print(f"Угадали! Попыток: {tries}")
        break

    print(f"Быков: {bulls}, коров: {cows}")
