from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    total1 = sum(queue1)
    total2 = sum(queue2)
    limit = (len(queue1) + len(queue2)) * 2
    
    if (total1 + total2) % 2 != 0:
        return -1
    target = (total1 + total2) // 2
    
    switch = 0
    while(total1 != total2):
        if total1 > total2:
            val = queue1.popleft()
            queue2.append(val)
            switch += 1
            
            total1 -= val
            total2 += val
        else:
            val = queue2.popleft()
            queue1.append(val)
            switch += 1
        
            total2 -= val
            total1 += val
            
        if switch > limit:
            return -1
    
    return switch