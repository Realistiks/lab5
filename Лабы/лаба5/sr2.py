print("Введите точность (например 0.000001)")
eps = float(input())

if eps <= 0:
    print("Точность должна быть положительной")
else:
    e = 1.0
    term = 1.0
    k = 1

    while term >= eps:
        term /= k
        e += term
        k += 1

    print(f"e = {e:.10f}")
    print("Членов ряда:", k - 1)
