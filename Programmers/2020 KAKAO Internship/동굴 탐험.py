def solution(n, path, order):
    path_dic = {}
    for p in path:
        x, y, = p[0], p[1]
        if x not in path_dic:
            path_dic[x] = []
        if y not in path_dic:
            path_dic[y] = []
        path_dic[x].append(y)
        path_dic[y].append(x)
    visit_first = {}
    visit_later = {}
    for o in order:
        x, y = o[0], o[1]
        if y not in visit_first:
            visit_first[y] = []
        if x not in visit_later:
            visit_later[x] = []
        visit_first[y].append(x)
        visit_later[x].append(y)
    visited = [0 for _ in range(n)]
    can_visit = [0 for _ in range(n)]
    can_visit[0] = 1
    visited[0] = 1
    queue = [0]
    if 0 in visit_first:
        return False
    while queue:
        current = queue.pop(0)
        can_go = True
        can_visit[current] = 1
        if current not in visit_first:
            visited[current] = 1
            for room in path_dic[current]:
                if visited[room] == 0:
                    queue.append(room)
            if current in visit_later and can_visit[visit_later[current][0]] == 1:
                queue.append(visit_later[current][0])
        else:
            if visited[visit_first[current][0]] == 1:
                visited[current] = 1
                for room in path_dic[current]:
                    if visited[room] == 0:
                        queue.append(room)

    answer = True if 0 not in can_visit else False
    return answer