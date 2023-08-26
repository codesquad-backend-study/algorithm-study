class Solution:
    def minWindow(self, s: str, t: str) -> str:

        mask = len(t)

        while mask <= len(s):
            for i in range(len(s) - mask + 1):
                window = s[i:i + mask]
                checker = list(t)

                for ch in window:
                    if ch in checker:
                        checker.remove(ch)

                if not checker:
                    return window

            mask += 1

        return ""


## 못 품