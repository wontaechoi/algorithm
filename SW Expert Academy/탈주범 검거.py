dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

tunnel = [[], [0,1,2,3], [0,2], [1,3], [0,1],[1,2],[2,3],[3,0]]
tunnel_possible = [[1,2,5,6], [1,3,6,7], [1,2,4,7],[1,3,4,5]]


T = int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnels = []
    for i in range(N):
        tunnels.append(list(map(int, input().split())))


    queue = [(R,C, 1)]
    visited = [(R,C)]
    while queue:
        x,y, t = queue.pop(0)
        if t == L:
            continue
        tun = tunnel[tunnels[x][y]]
        for i in tun:
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                continue

            if tunnels[new_x][new_y] not in tunnel_possible[i]:
                continue
            if (new_x,new_y) in visited:
                continue
            visited.append((new_x,new_y))
            queue.append((new_x, new_y, t+1))


    print("#{} {}".format(test_case, len(visited)))