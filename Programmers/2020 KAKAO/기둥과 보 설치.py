def check_possible(on_board):
    for x, y, a in on_board:
        if a == 0:  # 기둥
            if y == 0 or (x, y - 1, 0) in on_board or (x - 1, y, 1) in on_board or (x, y, 1) in on_board:
                continue
            else:
                return False
        else:
            if (x, y - 1, 0) in on_board or (x + 1, y - 1, 0) in on_board or (
                    (x - 1, y, 1) in on_board and (x + 1, y, 1) in on_board):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    board = [[0 for _ in range(n)] for __ in range(n)]
    on_board = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:  # 설치
            if check_possible(on_board + [(x, y, a)]):
                on_board.append((x, y, a))
        else:
            if (x, y, a) in on_board:
                on_board.pop(on_board.index((x, y, a)))
                if not check_possible(on_board):
                    on_board.append((x, y, a))
    answer = [list(i) for i in on_board]
    return sorted(answer, key=lambda x: [x[0], x[1], x[2]])