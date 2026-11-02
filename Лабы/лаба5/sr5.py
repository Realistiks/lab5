import random

print("Сколько точек бросить?")
n = int(input())

if n < 1:
    print("Количество точек должно быть больше 0")
else:
    inside = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inside += 1

    pi = 4 * inside / n
    print(f"Точек внутри: {inside} из {n}")
    print(f"pi = {pi:.4f}")
