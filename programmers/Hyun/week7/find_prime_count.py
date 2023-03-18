def solution(n, k):

    digits = []
    while n > 0:
        digits.append(n%k)
        n //= k
    digits.reverse()

    numbers = ''.join(map(str, digits)).split('0')
    nums = [number for number in numbers if number]
    nums = list(map(int, nums))

    cnt = len(nums)
    for num in nums:
        if num < 2:
            cnt -= 1

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                cnt -= 1
                break

    return cnt