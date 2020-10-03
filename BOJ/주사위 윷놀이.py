def sol(horses, horse_index, index, score):
    global board, answer, order
    if score + (10 - index)* 40 < answer:
        return
    if index == 10:
        answer = max(score, answer)
        return
    x, y = horses[horse_index]
    move = order[index]
    if x == 0:
        if y + move == len(board[x]) - 1:
            x, y = 4, 0
        elif y + move > len(board[x]) - 1:
            x, y = 4, 1
        elif (y + move) == 5:
            x, y = 1, 0
        elif (y + move) == 10:
            x, y = 2, 0
        elif (y + move) == 15:
            x, y = 3, 0
        else:
            x, y = 0, y + move

    elif x == 1 or x == 2 or x == 3:
        if y + move == len(board[x]) - 1:
            x, y = 4, 0
        elif y + move > len(board[x]) - 1:
            x, y = 4, 1
        else:
            x, y = x, y + move
    else:
        x, y = 4, 1

    if (x,y) != (4,1):
        if (x, y) in horses:
            return
        if (x,y) == (1, 4) or (x,y) == (2,3) or (x,y) == (3, 4):
            if (1,4) in horses or (2,3) in horses or (3,4) in horses:
                return
        if (x, y) == (1, 5) or (x, y) == (2, 4) or (x, y) == (3, 5):
            if (1, 5) in horses or (2, 4) in horses or (3, 5) in horses:
                return
        if (x,y) == (1, 6) or (x,y) == (2,5) or (x,y) == (3, 6):
            if (1,6) in horses or (2,5) in horses or (3,6) in horses:
                return
    horses[horse_index] = (x, y)
    score += board[x][y]
    found = False
    for h_i in range(4):
        if horses[h_i] != (4, 1):
            found = True
            sol(horses.copy(), h_i, index + 1, score)

    if not found:
        answer = max(score, answer)
    return




board = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
[10, 13, 16, 19, 25, 30, 35, 40],
[20, 22, 24, 25, 30, 35, 40],
[30, 28, 27, 26, 25, 30, 35, 40],
[40, 0]]


order = list(map(int, input().split()))
horses = [(0,0) for i in range(4)]
answer = 0
sol(horses, 0, 0, 0)
print(answer)