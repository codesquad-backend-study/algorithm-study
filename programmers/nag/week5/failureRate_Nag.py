import operator

def solution(N, stages):
    tried = []
    failed = []
    failureRate  = {}
    for i in range(N+1):
        tried.append(0)
        failed.append(0)
        failureRate[i] = 0
    del failureRate[0]
    
    for stage in stages:
        if stage <= N:
            failed[stage] += 1
            for i in range(1, stage + 1):
                tried[i] += 1
        else: 
            for i in range(1, N + 1):
                tried[i] += 1

    for i in range(1, N+1):
        if tried[i] == 0:
            failureRate[i] = 0
            continue
        failureRate[i] = failed[i] / tried[i]    
    sortedRate = sorted(failureRate.items(), key=operator.itemgetter(1), reverse = True)
    
    answer = []
    for tuple in sortedRate:
        answer.append(tuple[0])
    print(answer)
    return answer
