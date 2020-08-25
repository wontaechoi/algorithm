def drop(m, n, board):
    new_board = [[0 for j in range(n)] for i in range(m)]

    temp = [[] for i in range(n)]
    for j in range(n):
        for i in range(m - 1, -1, -1):
            if board[i][j] != 0:
                temp[j].append(board[i][j])
    for j in range(n):
        ind = m - 1
        for t in temp[j]:
            new_board[ind][j] = t
            ind -= 1

    return new_board


def check(m, n, board):
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    to_del = []
    for i in range(m - 1):
        for j in range(n - 1):
            pivot = board[i][j]
            if pivot != 0:
                if board[i][j + 1] == pivot and board[i + 1][j] == pivot and board[i + 1][j + 1] == pivot:
                    temp = [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]
                    for t in temp:
                        if t not in to_del:
                            to_del.append(t)
    for i, j in to_del:
        board[i][j] = 0
    return board, len(to_del)


def solution(m, n, board):
    new_board = []
    for b in board:
        new_board.append(list(b))
    answer = 0
    board = new_board
    while True:
        board, count = check(m, n, board)
        if count == 0:
            break
        answer += count
        board = drop(m, n, board)
    return answer