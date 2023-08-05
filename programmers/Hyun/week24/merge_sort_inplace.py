def merge_sort_inplace(arr, start, end):
    if end - start < 2:                 # 서브 리스트 길이가 1보다 작으면 종료
        return

    mid = (start + end) // 2
    merge_sort_inplace(arr, start, mid)
    merge_sort_inplace(arr, mid, end)

    sorted_list = []
    left, right = start, mid

    while left < mid and right < end:
        if arr[left] < arr[right]:
            sorted_list.append(arr[left])
            left += 1
        else:
            sorted_list.append(arr[right])
            right += 1

    while left < mid:
        sorted_list.append(arr[left])
        left += 1

    while right < end:
        sorted_list.append(arr[right])
        right += 1

    for i in range(start, end):
        arr[i] = sorted_list[i - start]


numbers = [9, 4, -80, 1, 172, 13, 9, 39, -99, 2054, 10, -10, 3, 67, -28]
merge_sort_inplace(numbers, 0, len(numbers))

print(numbers)
