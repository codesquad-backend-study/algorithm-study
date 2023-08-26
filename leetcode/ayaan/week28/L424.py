def characterReplacement(s, k):
    answer = 0
    i = 0
    while i < len(s) - k:
        count = k
        char = s[i]
        length = 1
        next_i = i + 1
        for j in range(i + 1, len(s)):
            if char != s[j]:
                if count == 0:
                    answer = max(answer, length)
                    break
                length += 1
                count -= 1
                next_i = j
            else:
                length += 1
        answer = max(answer, length)
        i = next_i
        if count > 0:
            return len(s)
    return answer

print(characterReplacement("ABAB", 2))
