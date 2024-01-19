def check_tree(bin_num):
    if len(bin_num) == 1:
        return True

    mid = len(bin_num) // 2
    mid_num = bin_num[mid]

    # 루트가 '0'일 때 아래에 '1'이 있으면 포화이진트리가 아님
    if mid_num == '0' and '1' in bin_num:
        return False

    # 왼쪽, 오른쪽 서브트리로 들어간다.
    left = check_tree(bin_num[:mid])
    right = check_tree(bin_num[mid + 1:])

    return left and right


def solution(numbers):
    answer = []

    for num in numbers:
        bin_num = bin(num)[2:]

        # 2^n - 1 = 포화이진트리 노드의 개수
        # 포화이진트리가 되도록 '0'을 앞에 붙여준다.
        depth = 1
        while (2 ** depth) - 1 < len(bin_num):
            depth += 1
        node_cnt = (2 ** depth) - 1
        bin_num = '0' * (node_cnt - len(bin_num)) + bin_num

        answer.append(int(check_tree(bin_num)))

    return answer


solution([10, 30, 50])
