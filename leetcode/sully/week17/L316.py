import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        answer = ''

        letters = collections.defaultdict(str)
        for c in s:
            letters[c] += 1

        # (letters[c] == 0)인 값 중 사전적으로 가장 먼저 오는 것을 찾아야 함
        tmp = []
        for i, c in enumerate(s):
            if letters[c] == 0:
                tmp.append((c, i))

        # c를 기준으로 오름차순 정렬
        tmp.sort(key=lambda x: x[0])

        # 그럼 이제 그리디 방식으로 여기부터 찾기 시작하면 됨
        # 왼쪽은 어차피 중복이니 볼 필요도 없는 거지
        start_index = tmp[0][1]

        # 앞에 거 안 보는 대신 value는 하나씩 빼줘야지
        for i in range(start_index + 1):
            letters[i] -= 1

        # 근데 이렇게 해주면 어차피 이 뒤에도 똑같이 비교해줘야 하는데 의미가 있나?
        for i in range(start_index, len(s)):
