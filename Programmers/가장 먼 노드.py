def solution(n, edge):
    vertex = {}
    for e in edge:
        e1, e2 = e[0], e[1]
        if e1 not in vertex:
            vertex[e1] = []
        if e2 not in vertex:
            vertex[e2] = []
        vertex[e1].append(e2)
        vertex[e2].append(e1)
    visited = [0 for _ in range(n)]
    ans = [n for _ in range(n)]
    ans[0] = 0
    stack = [(1, 0)]
    while stack:
        x, d = stack.pop(0)
        for v in vertex[x]:
            if ans[v - 1] > d + 1:
                ans[v - 1] = d + 1
                stack.append((v, d + 1))
    max_n = max(ans)
    answer = [n for n in ans if n == max_n]

    return len(answer)