dx = [-1,1, 0,0]
dy = [0,0,1,-1]

def catch(current, sharks):
    global R, C
    for i in range(R):
        if sharks[i][current] != 0 :
            score = sharks[i][current][2]
            sharks[i][current] = 0
            return score, sharks
    return 0, sharks

def move(sharks):
    new_sharks = [[0 for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            if sharks[i][j] != 0:
                s,d,z = sharks[i][j]
                new_x = i + (dx[d] * s)
                new_y = j + (dy[d] * s)
                if d == 0 :
                    if new_x < 0:
                        div,mod = divmod(abs(i + dx[d] * s), R-1)
                        if div % 2 == 0:
                            new_x = mod
                            d = d + 1
                        else:
                            new_x = R - 1 - mod
                            d= d if mod != 0 else d + 1
                elif d == 1:
                    if new_x >= R:

                        div, mod = divmod(abs(i + dx[d] * s), R-1)
                        if div % 2 != 0:
                            new_x = R - 1 - mod
                            d= d - 1
                        else:
                            new_x = mod
                            d = d if mod != 0 else d -1
                elif d == 2:
                    if new_y >= C:
                        div, mod = divmod(abs(j + dy[d] * s), C-1)
                        if div % 2 != 0:
                            new_y = C- 1 - mod
                            d = d + 1
                        else:
                            new_y = mod
                            d = d if mod != 0 else d + 1
                else:
                    if new_y < 0:
                        div, mod = divmod(abs(j + dy[d] * s), C-1)
                        if div % 2 == 0:
                            new_y = mod
                            d = d - 1
                        else:
                            new_y = C- 1 - mod
                            d = d if mod != 0 else d -1

                if new_sharks[new_x][new_y] == 0:
                    new_sharks[new_x][new_y] = (s,d,z)
                else:
                    c_s,c_d,c_z = new_sharks[new_x][new_y]
                    if c_z < z:
                        new_sharks[new_x][new_y] = (s,d,z)
    return new_sharks

R,C, M = map(int, input().split())
sharks = [[0 for i in range(C)] for j in range(R)]
for i in range(M):
    r,c,s,d,z = map(int, input().split())
    sharks[r-1][c-1] = (s,d-1,z)

answer = 0
for i in range(C):
    score, sharks = catch(i, sharks)
    answer += score
    sharks = move(sharks)
print(answer)