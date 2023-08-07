def quick_sort(arr, start, end):
    if end - start < 1:                 # 종료 조건, 데이터의 길이가 1이하
        return
    pivot = arr[end]                    # 가장 오른쪽 값이 피벗

    left = start
    right = end - 1
    while True:
        while arr[left] < pivot:            # 왼쪽부터 탐색, 피벗보다 큰 값이 있으면 stop
            left += 1
        while arr[right] > pivot:           # 오른쪽부터 탐색, 피벗보다 작은 값이 있으면 stop
            right -= 1
        if left >= right:                   # 왼쪽, 오른쪽 투 포인터가 같아지면 반복문 탈출
            break
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1                                          # 교환이 끝났으므로 투 포인터를 한 칸씩 이동

    arr[left], arr[end] = arr[end], arr[left]           # 마지막으로 피벗과 가운데 값을 교환
    quick_sort(arr, start, left - 1)                    # 피벗값의 좌측을 다시 퀵정렬
    quick_sort(arr, left + 1, end)                      # 피벗값의 우측을 다시 퀵정렬


# numbers = [9, 4, -80, 1, 172, 13, 9, 39, -99, 2054, 10, -10, 3, 67, -28]
numbers = [0, 1, 0]
quick_sort(numbers, 0, len(numbers) - 1)

print(numbers)
