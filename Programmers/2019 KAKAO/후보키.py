answer = 0
cand = []


def sol(row, index):
    global answer, cand
    for c in cand:
        count = len(c)
        for num in c:
            if num in index:
                count -= 1
        if count == 0:
            return

    n = len(row[0])
    check = ['' for _ in range(n)]
    for i in index:
        for j in range(n):
            check[j] += row[i][j]
    if len(set(check)) == n:
        answer += 1
        cand.append(index)
        return
    for i in range(len(row)):
        if i not in index:
            sol(row, index + [i])


def solution(relation):
    candidate = []
    row = [[] for _ in range(len(relation[0]))]
    for j, rel in enumerate(relation):
        for i, c in enumerate(rel):
            row[i].append(c)
    for i in range(len(row)):
        sol(row, [i])
    to_del = []

    for i in range(len(cand)):
        if i not in to_del:
            for j in range(len(cand)):
                if i != j:
                    count = len(cand[i])
                    for c in cand[i]:
                        if c in cand[j]:
                            count -= 1
                    if count == 0:
                        if j not in to_del:
                            to_del.append(j)
    return len(cand) - len(to_del)