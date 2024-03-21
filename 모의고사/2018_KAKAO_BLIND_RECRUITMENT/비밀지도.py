# 하나라도 벽(1)이면 -> 벽
# 둘다 공백(0)이면 -> 공백

def dec2bin(dec, n):
    bin = []
    while dec > 0:
        bin.append(dec % 2)
        dec //= 2
    bin = bin[::-1]
    if len(bin) < n:
        bin = [0] * (n - len(bin)) + bin
    return bin


def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        row1 = dec2bin(arr1[i], n)
        row2 = dec2bin(arr2[i], n)
        tmp = ""
        for j in range(n):
            if row1[j] == row2[j] and row1[j] == 0:
                tmp += " "
            else:
                tmp += "#"
        ans.append(tmp)
    return ans
