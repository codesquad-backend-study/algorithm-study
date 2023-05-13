def longest_palindrome_substring(str):
    def expand(left, right):
        while left >= 0 and right < len(str) and str[left] == str[right]:
            left -= 1
            right += 1
        return str[left + 1:right]

    if len(str) < 2 or str == str[::-1]:
        return str

    temp = ""
    for i in range(len(str) - 1):
        temp = max(temp, expand(i, i + 1), expand(i, i + 2), key=len)
    return temp


longest_palindrome_substring("babad")