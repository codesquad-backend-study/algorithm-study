class Solution:
    keys = {"2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        ans = []
        digits = list(digits)[::-1]

        self.make_str("", digits[:], ans)

        return ans

    def make_str(self, prev, digits, ans):
        if not digits:
            ans.append(prev)
            return

        digit = digits.pop()

        for ch in self.keys[digit]:
            self.make_str(prev + ch, digits[:], ans)
