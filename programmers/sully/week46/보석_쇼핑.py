from typing import List


# RUBY, DIA, EMERALD, SAPPHIRE
def solution(gems: List[str]) -> List[int]:
    answer = []
    # 초기 설정은 나올 수 없는 최대 거리로
    shortest_distance = len(gems) + 1
    lt, rt = 0, 0
    gems_hash = {}
    gems_type_count = len(set(gems))

    while rt < len(gems):
        if gems[rt] not in gems_hash:
            gems_hash[gems[rt]] = 1
        else:
            gems_hash[gems[rt]] += 1

        rt += 1

        gems_count = len(gems_hash)
        # 현재 구간에서 모든 종류의 보석이 있다면
        if gems_count == gems_type_count:
            while lt < rt:
                # lt에 해당하는 보석이 하나 그 이상일 시, 당연히 하나를 빼주기
                if gems_hash[gems[lt]] > 1:
                    gems_hash[gems[lt]] -= 1
                    lt += 1
                    continue

                # 현재 구간 거리가 최단 거리보다 짧다면
                if rt - lt < shortest_distance:
                    # 최단 거리 갱신
                    shortest_distance = rt - lt
                    # 배열상으로는 [lt, rt + 1]이 맞지만, 진열대 번호는 1부터 시작하니 이렇게 추가
                    answer = [lt + 1, rt]
                    break

                break

    return answer
