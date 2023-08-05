def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        pivot = arr[i]
        while j > 0 and pivot < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = pivot


numbers = [9, 4, -80, 1, 172, 13, 9, 39, -99, 2054, 10, -10, 3, 67, -28]

insertion_sort(numbers)

print(numbers)
