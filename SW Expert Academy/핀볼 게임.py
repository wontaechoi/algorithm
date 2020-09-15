dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
#to west, to east, to north, to south
block = [[0,1,2,3],
         [2,0, 3, 1],
         [3,0, 1, 2],
         [1,3, 0, 2],
         [1,2,3,0],
         [1,0,3,2]]


def sol(pos, i):
    start = pos
    x, y = pos
    score = 0
    while True:
        x, y = x + dx[i], y + dy[i]
        if x < 0 or x >= N or y < 0 or y >= N:
            i = i +1 if i % 2 == 0 else i -1
            score += 1
            continue
        if (x,y) == start:
            return score
        if board[x][y] == -1:
            return score
        if board[x][y] in [1,2,3,4,5]:
            score += 1
            i = block[board[x][y]][i]
            continue
        if board[x][y] in [6,7,8,9,10]:
            for q,w in wormhole[board[x][y]]:
                if (q,w) != (x,y):
                    x,y = q,w
                    break
            continue
test_case = int(input())
for t in range(1, test_case+1):
    N = int(input())
    board = []
    wormhole = {}
    start_position = []
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 0:
                start_position.append((i,j))
            if row[j] in [6,7,8,9,10]:
                if row[j] not in wormhole:
                    wormhole[row[j]] = []
                wormhole[row[j]].append((i,j))
        board.append(row)
    answer = 0
    for pos in start_position:
        for i in range(4):
            ans = sol(pos, i)
            answer = max(ans, answer)
    print("#{} {}".format(t, answer))

