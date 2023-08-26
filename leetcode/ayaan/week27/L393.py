def hammingWeight(n):
    count = 0
    while n:
        print(bin(n))
        n = n & (n - 1)
        print(bin(n))
        count += 1

    return count

hammingWeight(-3)
