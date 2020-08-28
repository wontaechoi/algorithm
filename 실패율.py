def solution(N, stages):
    fail = [0 for _ in range(N+1)]
    tried = [0 for _ in range(N+1)]
    for stage in stages:
        tried[stage-1] += 1
    for i in range(len(tried)):
        fail[i] = sum(tried[i:])
    ans = []
    for i in range(N):
        if fail[i] != 0:
            ans.append((i+1, (tried[i])/fail[i]))
        else:
            ans.append((i+1, 0))
    ans.sort(key = lambda x: [-x[1], x[0]])
    answer = []
    for a in ans:
        answer.append(a[0])
    return answer