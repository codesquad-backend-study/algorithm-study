class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open = {'(':0, '{':1, '[':2}
        close = {')':'(', '}':'{', ']':'['}
        for a in s:
            if a in open:
                stack.append(a)
            else :
                if len(stack) == 0:
                    return False
                tmp = stack.pop()
                if tmp != close[a]:
                    return False
        return True if len(stack) == 0 else False

        # dic = {'()':0, '{}':0, '[]':0}
        # for i in range(3):
        #     for a in dic:
        #         s = s.replace('a','')
        #         print(s)
        # return s == ''