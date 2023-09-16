def canCompleteCircuit(gas, cost):
    i = 0
    while i < len(gas):
        fuel = gas[i]
        if fuel < cost[i]:
            i += 1
            continue
        fuel -= cost[i]
        j = i + 1
        complete = True
        for _ in range(len(gas) - 1):
            fuel += gas[j % len(gas)]
            if fuel < cost[j % len(gas)]:
                i = j
                complete = False
                break
            fuel -= cost[j % len(gas)]
            j += 1
        if complete:
            return i
        i += 1
    return -1


print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
