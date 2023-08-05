def merge_sort(arr):
    if len(arr) < 2:                        # 리스트 길이가 1 이하인 경우, 더 이상 쪼갤 수 없으므로 재귀 종료
        return arr

    mid = len(arr) // 2

    left_arr = merge_sort(arr[:mid])            # 가운데를 기준으로 왼쪽 분할
    right_arr = merge_sort(arr[mid:])           # 가운데를 기준으로 오른쪽 분할

    sorted_list = []
    left = right = 0

    while left < len(left_arr) and right < len(right_arr):          # 분할된 두 리스트를 정렬하며 합치기
        if left_arr[left] < right_arr[right]:
            sorted_list.append(left_arr[left])
            left += 1
        else:
            sorted_list.append(right_arr[right])
            right += 1

    while left < len(left_arr):
        sorted_list.append(left_arr[left])
        left += 1

    while right < len(right_arr):
        sorted_list.append(right_arr[right])
        right += 1

    return sorted_list                              # 합쳐진 (정렬된) 리스트를 반환


numbers = [9, 4, -80, 1, 172, 13, 9, 39, -99, 2054, 10, -10, 3, 67, -28]
print(merge_sort(numbers))
