from typing import List


def letterCombinations(digits: str) -> List[str]:
    phone = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    def findWord(index, path):
        if len(path) == len(digits):
            answer.append(path)
            return

        for j in phone[digits[index]]:
            findWord(index + 1, path + j)

    if not digits:
        return []

    answer = []
    findWord(0, "")
    print(answer)

    return answer


letterCombinations("23")
