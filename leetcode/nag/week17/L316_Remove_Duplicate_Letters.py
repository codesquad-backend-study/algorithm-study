class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        length = len(set(s))
        candidate = set()
        copy = s[:]
        while copy:
            temp = ""
            for char in copy:
                if char not in temp:
                    temp = temp + char
            if len(temp) == length:
                candidate.add(temp)
            copy = copy[1:]
        copy = s[::-1]
        while copy:
            temp = ""
            for char in copy:
                if char not in temp:
                    temp = char + temp
            if len(temp) == length:
                candidate.add(temp)
            copy = copy[1:]
        sortedCandidate = sorted(candidate)
        return sortedCandidate[0]

