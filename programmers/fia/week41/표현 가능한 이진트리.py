def recover(binary, index, depth):
    if depth == 0:  # 리프 노드에 도달했다면
        return 1  # 포화이진트리

    # 부모 노드가 0일 때, 왼쪽 or 오른쪽 자식 노드가 1일 수 없다.
    elif binary[index] == '0':
        if binary[index - depth] == '1' or binary[index + depth] == '1':
            return 0

    left = recover(binary, index - depth, depth // 2)
    right = recover(binary, index + depth, depth // 2)

    return left and right


def solution(numbers):
    # 포화이진트리에서 전체 노드의 개수는 2^n-1이다.
    # 따라서 노드의 개수 + 1 = 2^n을 만족해야 한다.
    # 2^n은 이진수로 변환하면 첫 번째 자리만 1, 나머지는 0이다. ex. 10000
    # 이를 이용해서 포화이진트리인지 확인할 수 있다.

    results = []

    for number in numbers:
        number_bin = bin(number)[2:]
        nodes = bin(len(number_bin) + 1)[2:]

        if '1' in nodes[1:]:  # 포화이진트리가 아닌 경우
            dummy = (1 << len(nodes)) - int(nodes, 2)
            number_bin = '0' * dummy + number_bin

        results.append(recover(number_bin, len(number_bin) // 2, (len(number_bin) + 1) // 4))

    return results


print(solution([7, 42, 5]))


# -------------------------

def solution(numbers):
    return [int(expressible(number)) for number in numbers]


def expressible(number):
    binary = convert_to_full_binary(number)
    return check(binary)


def convert_to_full_binary(number):
    binary = bin(number)[2:]
    n, s = 0, 1  # 2의 제곱수 n, 노드 수 s

    while len(binary) > s:
        n += 1
        s += 2 ** n

    return '0' * (s - len(binary)) + binary


def check(binary, is_parent_dummy=False):
    if len(binary) == 1:
        return not is_parent_dummy or binary == '0'

    root_index = len(binary) // 2
    root = binary[root_index]

    if is_parent_dummy and root == '1':
        return False

    is_parent_dummy = is_parent_dummy or root == '0'

    return check(binary[:root_index], is_parent_dummy) and check(binary[root_index + 1:], is_parent_dummy)
