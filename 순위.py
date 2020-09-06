def solution(n, results):
    win = {}
    lost = {}
    for i in range(1, n + 1):
        win[i] = set()
        lost[i] = set()
    for r in results:
        x, y = r[0], r[1]
        if x not in win:
            win[x] = []
        if y not in lost:
            lost[y] = []
        win[x].add(y)
        lost[y].add(x)

    for i in range(n):
        for y in lost[i + 1]:
            win[y].update(win[i + 1])
        for x in win[i + 1]:
            lost[x].update(lost[i + 1])

    answer = 0
    for i in range(1, n + 1):
        if len(win[i].union(lost[i])) == n - 1:
            answer += 1
    return answer