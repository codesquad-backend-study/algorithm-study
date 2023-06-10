def lengthOfLongestSubstring(self, s: str) -> int:
    def checkRepeatingCharacters(target):
        char_dict = collections.defaultdict(int)
        for ch in target:
            if ch in char_dict:
                return False
            char_dict[ch] += 1
        return True

    if len(s) == 0:
        return 0
    result = 1
    for i in range(len(s)):
        if i + result + 1 > len(s) + 1:
            break
        if not checkRepeatingCharacters(s[i:i + result + 1]):
            continue
        for j in range(i + result + 1, len(s) + 1):
            word = s[i:j]
            if not checkRepeatingCharacters(word):
                break
            result = j - i
    return result
