def play(board, move):
    N = len(board)
    for i in range(N):
        if board[i][move] > 0:
            doll = board[i][move]
            board[i][move] = 0
            return board, doll
    return board, -1


def solution(board, moves):
    picked = []
    answer = 0
    for move in moves:
        board, doll = play(board, move - 1)
        if doll != -1:
            if len(picked) >= 1:
                if picked[-1] == doll:
                    picked = picked[:-1]
                    answer += 2
                    continue
        picked.append(doll)

    return answer