dx = [-1, -1,-1,0,0,1,1,1]
dy = [-1, 0,1,-1,1,-1,0,1]
def year(ground,  trees):
    global N, eat
    new_trees = [[[] for _ in range(N)] for __ in range(N)]
    new_ground = [[0 for _ in range(N)] for __ in range(N)]
    for x in range(N):
        for y in range(N):
            if trees[x][y]:
                trees[x][y].sort()
                cnt = 0
                for n in range(len(trees[x][y])):
                    z = trees[x][y][n]
                    gr = ground[x][y]
                    if gr >= z:
                        ground[x][y] -= z
                        new_trees[x][y].append(z +1)
                        if (z+1)% 5 == 0:
                            cnt += 1
                    else:
                        new_ground[x][y] += z // 2
                if cnt >= 1:
                    for i in range(8):
                        new_x = x + dx[i]
                        new_y = y + dy[i]
                        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                            continue
                        new_trees[new_x][new_y] += [1]*cnt
            ground[x][y] += eat[x][y] + new_ground[x][y]
    return ground, new_trees
N,M,K = map(int,input().split())
eat = []
for i in range(N):
    eat.append(list(map(int,input().split())))
ground = [[5 for i in range(N)] for j in range(N)]
trees = [[[] for _ in range(N)] for __ in range(N)]
for i in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)
for i in range(K):
    ground, trees = year(ground,  trees)

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])
print(answer)