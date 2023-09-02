import sys


def minWindow(s, t):
    answer = s
    i = 0
    while i <= len(s) - len(t):
        match = {}
        for ch in t:
            match[ch] = False

        next_i = i + 1
        for j in range(i, len(s)):
            if s[j] in match:
                match[s[j]] = True
                if sum(match.values()) == 2:
                    next_i = j
                elif sum(match.values()) == 3:
                    if len(answer) > j - i + 1:
                        answer = s[i:j+1]
                    break
        i = next_i
        if sum(match.values()) == 0:
            return ""

    return answer

print(minWindow("ADOBECODEBANC", "ABC"))
