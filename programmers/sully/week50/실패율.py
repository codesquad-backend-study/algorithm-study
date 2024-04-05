def solution(N, stages):
    failure_rates = {}
    mo = len(stages)

    for i in range(1, N + 1):
        za = stages.count(i)

        if mo == 0:
            failure_rates[i] = 0
        else:
            failure_rates[i] = za / mo

        mo -= za

    sorted_stages = sorted(failure_rates.keys(), key=lambda x: failure_rates[x], reverse=True)

    return sorted_stages


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
