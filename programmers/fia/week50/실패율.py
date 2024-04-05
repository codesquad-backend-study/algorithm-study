from collections import Counter


def solution(N, stages):
    answer = []
    stages = Counter(stages)
    passed = 0

    for current_stage in range(N + 1, 0, -1):
        clear = 0
        if current_stage in stages:
            passed += stages[current_stage]
            clear = stages[current_stage] / passed
        answer.append((clear, current_stage))

    answer.sort(key=lambda x: (x[0], -x[1]), reverse=True)

    return [element[1] for element in answer if element[1] <= N]
