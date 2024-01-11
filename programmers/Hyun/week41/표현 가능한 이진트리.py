def solution(numbers):
    def make_tree(number):
        if len(number) == 1:
            return number[0]

        mid = len(number) // 2

        left = make_tree(number[:mid])
        right = make_tree(number[mid + 1:])

        global flag

        if flag and number[mid] == '0':
            if left == '1' or right == '1':
                flag = False

        return number[mid]

    global flag
    ans = []
    for num in numbers:
        binary = bin(num)[2:]
        n, node_cnt = 0, 1

        while len(binary) > node_cnt:
            n += 1
            node_cnt += 2 ** n

        binary = binary.zfill(node_cnt)

        flag = True
        make_tree(binary)
        if flag:
            ans.append(1)
        else:
            ans.append(0)

    return ans

