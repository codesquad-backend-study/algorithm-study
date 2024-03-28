# 길이가 1인 모든 단어를 포함하도록 사전 초기화
# 주어진 입력에서 사전에 있는 가장 긴 문자열을 찾는다.
# 사전 색인 번호를 출력하고, 해당 문자열은 제거한다.
# 처리되지 않은 다음 글자를 포함한 단어를 사전에 등록한다.
# 숫자 인덱스들을 결과 리스트로 반환한다.
def solution(msg):
    dictionary = {chr(ord('A') + i): i + 1 for i in range(26)}

    ans = []
    idx = 27
    s = 0
    while True:
        if msg[s:] in dictionary:
            ans.append(dictionary[msg[s:]])
            break

        for i in range(s + 1, len(msg) + 1):
            if msg[s:i] not in dictionary:
                dictionary[msg[s:i]] = idx
                idx += 1
                ans.append(dictionary[msg[s:i - 1]])
                s = i - 1
                break

    return ans
