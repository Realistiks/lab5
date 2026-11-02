print("Напишите число")
n = int(input())
first = n
prost = []
div = 2
while div * div <= n:
    while n % div == 0:
        prost.append(div)
        n //= div
    div += 1
if n > 1:
    prost.append(n)

if len(prost) == 0:
    print("Нужно число не меньше 2")
elif prost == [first]:
    print(f"{first} - простое число")
else:
    print(f"{first} = " + " × ".join(str(x) for x in prost))
