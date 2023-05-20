from typing import List


class Solution:
    # logs: 사전순으로 정렬 (문자 먼저 정렬되고, 숫자는 상대적인 순서 유지)
    # 문자와 숫자의 순서 정렬 문제니까 lambda 써보자!
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []

        for log in logs:
            identifier, words = log.split(" ", 1)
            if log.split()[1].isalpha():
                letters.append((identifier, words))
            else:
                digits.append(log)

        letters.sort(key=lambda x: (x[1], x[0]))

        real_letters = []
        for letter in letters:
            real_letters.append(" ".join(letter))

        return real_letters + digits


print(Solution().reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
