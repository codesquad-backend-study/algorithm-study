def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        result = []
        row1 = format(arr1[i], 'b').zfill(n)
        row2 = format(arr2[i], 'b').zfill(n)

        for j in range(n):
            if row1[j] == '1' or row2[j] == '1':
                result.append('#')
            else:
                result.append(" ")

        answer.append("".join(result))

    return answer
