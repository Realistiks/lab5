print("Прямоугольник")
n = int(input("N = "))
m = int(input("M = "))
for i in range(n):
    print("*" * m)

print()
print("Треугольник")
n = int(input("N = "))
for i in range(1, n + 1):
    print("*" * i)

print()
print("Ёлочка")
n = int(input("N = "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print()
print("Ромб")
n = int(input("N = "))

sizes = list(range(1, n + 1, 2))
if n % 2 == 0:
    sizes = sizes + [sizes[-1]] + sizes[-2::-1]
else:
    sizes = sizes + sizes[-2::-1]

width = max(sizes)
for s in sizes:
    print(" " * ((width - s) // 2) + "*" * s)
