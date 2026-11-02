print("Введите число")
n = int(input())

x = abs(n)
reversed_num = 0
t = x

while t > 0:
    reversed_num = reversed_num * 10 + t % 10
    t //= 10

if reversed_num == x:
    print(f"{n} — палиндром")
else:
    print(f"{n} — не палиндром")
