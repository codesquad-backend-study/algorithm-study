def hammingDistance(x, y):
    count = 0
    while x != 0 or y != 0:
        if x % 2 ^ y % 2:
            count += 1
        x = x // 2
        y = y // 2
    print(count)

hammingDistance(1, 4)
