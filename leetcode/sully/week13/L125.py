class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. 알파벳 제외한 모든 문자 제거
        for w in s:
            # 알파벳이 아니라면 그 문자는 다 없애주기
            if not w.isalpha() and not w.isdigit():
                s = s.replace(w, '')

        # 2. lowerCase
        s = s.lower()

        # 3. 뒤집어도 같은지 비교
        # 0P는 False, a는 True
        # if len(s) == 2:
        #     if s[0] == s[1]:
        #         return True
        #     else:
        #         return False
        #
        # if len(s) % 2 == 0:
        #     if s[:len(s) // 2 + 1] == s[len(s) // 2 + 1:][::-1]:
        #         return True
        #     else:
        #         return False
        # else:
        #     if s[:len(s) // 2] == s[len(s) // 2 + 1:][::-1]:
        #         return True
        #     else:
        #         return False

        answer = True
        lt, rt = 0, len(s) - 1
        if len(s) % 2 == 0:
            for _ in range(len(s) // 2):
                print(s[lt], s[rt])
                if s[lt] != s[rt]:
                    return False
                lt += 1
                rt -= 1
        else:
            for _ in range(len(s) // 2 + 1):
                print(s[lt], s[rt])
                if s[lt] != s[rt]:
                    return False
                lt += 1
                rt -= 1

        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
