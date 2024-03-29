def solution(alp, cop, problems):
    max_alp = -1
    max_cop = -1
    for alp_req, cop_req, _, _, _ in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)

    times = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]

    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    times[alp][cop] = 0

    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            if a + 1 <= max_alp:
                times[a + 1][c] = min(times[a + 1][c], times[a][c] + 1)
            if c + 1 <= max_cop:
                times[a][c + 1] = min(times[a][c + 1], times[a][c] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    na = min(max_alp, a + alp_rwd)
                    nc = min(max_cop, c + cop_rwd)
                    times[na][nc] = min(times[na][nc], times[a][c] + cost)

    return times[-1][-1]
