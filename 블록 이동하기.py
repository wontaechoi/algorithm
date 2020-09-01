dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(board):
    N = len(board)
    answer = 0
    visited = [(0, 0, 1)]
    queue = [(0, 0, 1, 0)]
    c = 0
    while queue:
        x1, y1, d, t = queue.pop(0)
        x2, y2 = x1 + dx[d], y1 + dy[d]

        if (x1, y1) == (N - 1, N - 1) or (x2, y2) == (N - 1, N - 1):
            answer = t
            break
        for i in range(4):
            new_x1 = x1 + dx[i]
            new_y1 = y1 + dy[i]
            new_x2 = x2 + dx[i]
            new_y2 = y2 + dy[i]
            if new_x1 < 0 or new_x1 >= N or new_x2 < 0 or new_x2 >= N or new_y1 < 0 or new_y1 >= N or new_y2 < 0 or new_y2 >= N:
                continue
            if board[new_x1][new_y1] == 1:
                continue
            if board[new_x2][new_y2] == 1:
                continue
            if (new_x1, new_y1, d) in visited or (new_x2, new_y2, (d + 2) % 4) in visited:
                continue
            visited.append((new_x1, new_y1, d))
            queue.append((new_x1, new_y1, d, t + 1))
        if d % 2 != 0:
            if x1 - 1 >= 0 and x2 - 1 >= 0:
                if board[x1 - 1][y1] == 0 and board[x2 - 1][y2] == 0:
                    if (x1 - 1, y1, 2) not in visited and (x1, y1, 0) not in visited:
                        visited.append((x1 - 1, y1, 2))
                        queue.append((x1 - 1, y1, 2, t + 1))
                    if (x2 - 1, y2, 2) not in visited and (x2, y2, 0) not in visited:
                        visited.append((x2 - 1, y2, 2))
                        queue.append((x2 - 1, y2, 2, t + 1))
            if x1 + 1 < N and x2 + 1 < N:
                if board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:
                    if (x1 + 1, y1, 0) not in visited and (x1, y1, 2) not in visited:
                        visited.append((x1 + 1, y1, 0))
                        queue.append((x1 + 1, y1, 0, t + 1))
                    if (x2 + 1, y2, 0) not in visited and (x2, y2, 2) not in visited:
                        visited.append((x2 + 1, y2, 0))

                        queue.append((x2 + 1, y2, 0, t + 1))
        else:
            if y1 - 1 >= 0 and y2 - 1 >= 0:
                if board[x1][y1 - 1] == 0 and board[x2][y2 - 1] == 0:
                    if (x1, y1 - 1, 1) not in visited and (x1, y1, 3) not in visited:
                        visited.append((x1, y1 - 1, 1))
                        queue.append((x1, y1 - 1, 1, t + 1))
                    if (x2, y2 - 1, 1) not in visited and (x2, y2, 3) not in visited:
                        visited.append((x2, y2 - 1, 1))
                        queue.append((x2, y2 - 1, 1, t + 1))
            if y1 + 1 < N and y2 + 1 < N:
                if board[x1][y1 + 1] == 0 and board[x2][y2 + 1] == 0:
                    if (x1, y1 + 1, 3) not in visited and (x1, y1, 1) not in visited:
                        visited.append((x1, y1 + 1, 3))
                        queue.append((x1, y1 + 1, 3, t + 1))
                    if (x2, y2 + 1, 3) not in visited and (x2, y2, 1) not in visited:
                        visited.append((x2, y2 + 1, 3))
                        queue.append((x2, y2 + 1, 3, t + 1))
    return answer