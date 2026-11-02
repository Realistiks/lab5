print("Введите числа через пробел")
arr = [int(x) for x in input().split()]

for i in range(len(arr) - 1):
    swapped = False
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break

print("Отсортировано:", " ".join(str(x) for x in arr))
