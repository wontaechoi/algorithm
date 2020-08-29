def check2(board):
    ##
    ##
    ##
    N = len(board)
    to_del = []
    count = 0
    for i in range(N - 2):
        for j in range(N - 1):
            count_1 = 0
            count_b = 0
            current_b = -2
            flag = False
            for x in range(3):
                for y in range(2):
                    if board[i + x][j + y] == 0:
                        flag = True
                        break
                    elif board[i + x][j + y] == -1:
                        count_1 += 1
                        if count_1 > 2:
                            flag = True
                            break
                    else:
                        if current_b == -2:
                            current_b = board[i + x][j + y]
                            count_b += 1
                        else:
                            if current_b != board[i + x][j + y]:
                                flag = True
                                break
                            count_b += 1

                if flag:
                    break
            if not flag:
                count += 1
                for x in range(3):
                    for y in range(2):
                        if (i + x, j + y) not in to_del:
                            to_del.append((i + x, j + y))
    return to_del, count


def check1(board):
    ###
    ###
    N = len(board)
    to_del = []
    count = 0
    for i in range(N - 1):
        for j in range(N - 2):
            count_1 = 0
            count_b = 0
            current_b = -2
            flag = False
            for x in range(2):
                for y in range(3):
                    if board[i + x][j + y] == 0:
                        flag = True
                        break
                    elif board[i + x][j + y] == -1:
                        count_1 += 1
                        if count_1 > 2:
                            flag = True
                            break
                    else:
                        if current_b == -2:
                            current_b = board[i + x][j + y]
                            count_b += 1
                        else:
                            if current_b != board[i + x][j + y]:
                                flag = True
                                break
                            count_b += 1

                if flag:
                    break
            if not flag:
                count += 1
                for x in range(2):
                    for y in range(3):
                        if (i + x, j + y) not in to_del:
                            to_del.append((i + x, j + y))
    return to_del, count


def solution(board):
    answer = 0
    N = len(board)
    while True:
        black = []
        for j in range(N):
            flag = False
            for i in range(N):
                if board[i][j] != 0:
                    flag = True
                    break
                else:
                    black.append((i, j))

        for i, j in black:
            board[i][j] = -1
        l1, c1 = check1(board)
        l2, c2 = check2(board)
        if c1 == 0 and c2 == 0:
            break
        to_del = list(set(l1 + black + l2))
        answer += c1 + c2
        for i, j in to_del:
            board[i][j] = 0
    return answer