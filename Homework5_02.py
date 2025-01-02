def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iteration = 0
    upper_bound = None

    while low <= high:
        iteration += 1
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
            upper_bound = arr[mid]       
        else:
            return (arr[mid], iteration,)
    return (iteration, upper_bound)

# Тестуємо наш бінарний пошук:

arr = [1.11, 2.22, 3.33, 4.44, 5.55, 6.66, 7.77, 8.88, 9.99]
target = 7.0
result = binary_search(arr, target)
print(f"Кількість ітерацій: {result[0]}, Верхня границя: {result[1]}")