from typing import List


def solution(user_id: List[str], banned_id: List[str]) -> int:
    possible_bad_users = make_possible_bad_users(banned_id, user_id)
    answer = find_bad_users(banned_id, possible_bad_users)
    return len(answer)


def find_bad_users(banned_id, possible_bad_users):
    answer = set()
    stack = [(set(), 0)]

    while stack:
        current, _id = stack.pop()

        # 레벨이 금지된 id의 개수와 같다면, 현재 조합은 금지된 id에 대한 조합을 포함하고 있다는 거임
        # 즉, 그렇다면 현재 조합을 정렬하여 집합에 추가할 수 있도록 tuple로 변환하여 추가
        if _id == len(banned_id):
            answer.add(tuple(sorted(current)))
            continue

        for x in possible_bad_users[_id]:
            # 조합에 존재하지 않다면, 새로운 조합을 만들어 스택에 추가 후 계속 선회
            if x not in current:
                _next = current.union({x})
                stack.append((_next, _id + 1))

    return answer


def make_possible_bad_users(banned_id, user_id):
    possible_bad_users = []

    for bid in banned_id:
        tmp = []
        for uid in user_id:

            if len(uid) == len(bid):
                flag = True

                for i in range(len(uid)):
                    if (uid[i] != bid[i]) and (bid[i] != '*'):
                        flag = False
                        break

                if flag:
                    tmp.append(uid)

        possible_bad_users.append(tmp)

    return possible_bad_users
