import random


def quick_sort(arr, start, end):
    if end - start < 1:
        return

    rand = random.randrange(start, end + 1)
    pivot = arr[rand]
    arr[rand], arr[end] = arr[end], arr[rand]  # 피벗을 랜덤으로 정한 뒤, 맨 끝으로 이동

    left = start
    right = end - 1

    while True:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left >= right:
            break

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    arr[left], arr[end] = arr[end], arr[left]

    quick_sort(arr, start, left - 1)
    quick_sort(arr, left + 1, end)


numbers = [9, 4, -80, 1, 172, 13, 9, 39, -99, 2054, 10, -10, 3, 67, -28]

quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)
