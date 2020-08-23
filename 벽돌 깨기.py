def find_brick(col, board):
    global W, H
    for r in range(H):
        if board[r][col] > 0:
            return r
    return -1

def drop(board):
    global W, H
    new_board = [[0 for i in range(W)] for j in range(H)]
    temp =[]
    for w in range(W):
        t = []
        for h in range(H-1, -1, -1):
            if board[h][w] != 0:
                t.append(board[h][w])
        temp.append(t)

    w, h = 0, H-1
    for t in temp:
        for n in t:
            new_board[h][w] = n
            h -=1
        w +=1
        h = H-1
    return new_board

def bomb(row,col,board):
    global W, H
    dx = [0,0,-1,1]
    dy = [-1,1, 0,0]
    stack = [(row,col, board[row][col])]
    visited = [[0 for i in range(W)] for j in range(H)]
    visited[row][col] = 1
    while stack:
        x,y,n = stack.pop(0)
        for i in range(4):
            new_x = x
            new_y = y
            for j in range(1, n):
                new_x += dx[i]
                new_y += dy[i]
                if new_x <0 or new_x >= H or new_y < 0 or new_y >= W:
                    break
                if visited[new_x][new_y] == 1:
                    continue
                visited[new_x][new_y] = 1
                if board[new_x][new_y] != 0:
                    stack.append((new_x,new_y,board[new_x][new_y]))
    new_board = [[0 for i in range(W)] for j in range(H)]
    for i in range(H):
        for j in range(W):
            if visited[i][j] ==1:
                new_board[i][j] = 0
            else:
                new_board[i][j] = board[i][j]
    return new_board

def calc(board):
    global W, H
    count = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] > 0:
                count +=1
    return count
def sol(n, col, board,path):
    global answer, W, H
    if n == 0:
        if calc(board) < answer:
            answer = calc(board)
        return
    row = find_brick(col, board)
    if row != -1:
        board = bomb(row, col, board)
        board = drop(board)
    for i in range(W):
        sol(n-1, i, board, path + [i])

test_case = int(input())
for t in range(1, test_case +1):
    N, W, H = map(int, input().split())
    board= []
    answer = float('inf')
    for i in range(H):
        board.append(list(map(int, input().split())))

    for i in range(W):
        sol(N, i, board, [i])



    print("#{} {}".format(t, answer))
