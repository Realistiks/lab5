import math

print("Табуляция функции y = sin(x) от 0 до pi с шагом pi/10")
print()
print(f'{"x":>10} | {"sin(x)":>10}')
print("-" * 23)

x = 0.0
step = math.pi / 10

while x <= math.pi + step / 2:
    print(f'{x:>10.4f} | {math.sin(x):>10.4f}')
    x += step
