def sol(circle, x, d, k):
    global N, M
    new_circle = []
    for i in range(N):
        if (i + 1) % x == 0:
            if d == 1:
                new_circle.append(circle[i][k:] + circle[i][:k])
            else:
                new_circle.append(circle[i][M-k:] + circle[i][:M-k])
        else:
            new_circle.append(circle[i])
    to_del = set()
    total = 0
    num = 0
    for i in range(N):
        for j in range(M):
            if new_circle[i][j] != 'x':
                if i == 0 or i < N- 1:
                    if new_circle[i][j] == new_circle[i+1][j]:
                        to_del.add((i,j))
                        to_del.add((i+1,j))
                elif i == N-1 or i > 0:
                    if new_circle[i][j] == new_circle[i - 1][j]:
                        to_del.add((i, j))
                        to_del.add((i - 1, j))

                if j == 0:
                    if new_circle[i][j] == new_circle[i][1]:
                        to_del.add((i,j))
                        to_del.add((i,1))
                    elif new_circle[i][j] == new_circle[i][M-1]:
                        to_del.add((i, j))
                        to_del.add((i, M-1))
                elif j == M - 1:
                    if new_circle[i][j] == new_circle[i][0]:
                        to_del.add((i,j))
                        to_del.add((i,0))
                    elif new_circle[i][j] == new_circle[i][j-1]:
                        to_del.add((i, j))
                        to_del.add((i, j - 1))
                else:
                    if new_circle[i][j] == new_circle[i][j+1]:
                        to_del.add((i,j))
                        to_del.add((i,j+1))
                    elif new_circle[i][j] == new_circle[i][j-1]:
                        to_del.add((i, j))
                        to_del.add((i, j - 1))
                total += new_circle[i][j]
                num += 1
    if num == 0:
        return new_circle
    avg = total / num
    if len(list(to_del)) == 0:
        for i in range(N):
            for j in range(M):
                if new_circle[i][j] != 'x':
                    if new_circle[i][j] > avg:
                        new_circle[i][j] -= 1
                    elif new_circle[i][j] < avg:
                        new_circle[i][j] += 1
    else:
        for x, y in list(to_del):
            new_circle[x][y] = 'x'
    return new_circle



N, M, T = map(int, input().split())
circle = []
for i in range(N):
    circle.append(list(map(int, input().split())))

rotate = []
for i in range(T):
    x, d, k = map(int, input().split())
    rotate.append((x, d, k))

for x, d, k in rotate:
    circle = sol(circle, x,d, k)
answer = 0
for i in range(N):
    for j in range(M):
        if circle[i][j] != 'x':
            answer += circle[i][j]
print(answer)