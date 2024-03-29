# 노드: 현재 key 값, 자식 노드들, 값 존재 여부
def solution(words):
    root = ["root", {}, False]  # 트라이 만들기
    for word in words:
        cur = root
        for ch in word:
            if ch not in cur[1]:
                node = [ch, {}, False]
                cur[1][ch] = node
            cur = cur[1][ch]
        cur[2] = word

    ans = 0
    for word in words:  # 트라이에서 모든 단어 검색
        cur = root
        cnt = 0
        for idx, ch in enumerate(word):
            if len(cur[1]) > 1:  # 트라이가 갈라지면, 해당 인덱스 + 1 까지 입력해야함
                cnt = idx + 1
            if cur[2]:  # 검색도중 단어값을 지나치면, 해당 단어 인덱스 + 1 까지 입력해야함
                cnt = idx + 1
            cur = cur[1][ch]

        if len(cur[1]) > 0:  # 단어를 찾았는데, 해당 단어를 포함하는 더 긴 단어가 있으면 해당 단어를 모두 입력해야함
            cnt = len(word)

        ans += cnt

    return ans
