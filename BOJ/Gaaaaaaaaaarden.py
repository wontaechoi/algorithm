from itertools import combinations

def sol(green_position, red_position):
    global N, M, possible, answer
    queue = []
    visited = {}
    for pos in list(green_position):
        x, y = possible[pos]
        queue.append((x, y, 0, 0))
        visited[(x,y)] = (0,0)
    for pos in list(red_position):
        x, y = possible[pos]
        queue.append((x, y, 0, 1))
        visited[(x, y)] = (0, 1)
    count = 0
    while queue:
        x, y, t, c = queue.pop(0)
        if visited[(x, y)][1] != 2:
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M or garden[new_x][new_y] == 0:
                    continue
                if (new_x, new_y) in visited:
                    c_t, c_c = visited[(new_x, new_y)]
                    if c_c == 2 or c_t < t + 1:
                        continue
                    elif c_t > t + 1:
                        visited[(new_x, new_y)] = (t + 1, c)
                        queue.append((new_x, new_y, t + 1, c))
                    elif c_t == t + 1 and c_c != c:
                        visited[(new_x, new_y)] = (t + 1, 2)
                        count += 1
                else:
                    visited[(new_x, new_y)] = (t + 1, c)
                    queue.append((new_x, new_y, t + 1, c))

    answer = max(count, answer)
    return


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N, M, G, R = map(int, input().split())
possible = []
garden = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 2:
            possible.append((i,j))
    garden.append(row)

green_positions = list(combinations([i for i in range(len(possible))], G))

answer = 0
for green_position in green_positions:
    red_positions = list(combinations([i for i in range(len(possible)) if i not in list(green_position)], R))
    for red_position in red_positions:
        sol(green_position, red_position)
print(answer)
