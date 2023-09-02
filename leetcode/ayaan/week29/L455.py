import collections

def findContentChildren(g, s):
    g.sort()
    g = collections.deque(g)
    s.sort()
    result = 0

    for cookie in s:
        if g and g[0] <= cookie:
            g.popleft()
            result += 1
    return result
