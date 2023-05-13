class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_tups = []

        for log in logs:
            id, content = log.split(" ", 1)
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_tups.append((id, content))

        letter_tups.sort(key=lambda x: (x[1], x[0]))

        ans = []
        for tup in letter_tups:
            ans.append(" ".join(tup))

        ans.extend(digit_logs)

        return ans
