dx = [-1,0,1,0]
dy = [0, 1, 0, -1]
def solution(board):
    N = len(board)
    finish = (N-1, N-1)
    queue = [(0,0,0,-1)]
    visited ={(0,0):0}
    answer = float('inf')
    while queue:
        x,y ,cost, d = queue.pop(0)
        if (x,y) == finish:
            answer = min(answer, cost)
            continue
        for i in range(4):
            new_x = x +dx[i]
            new_y = y+ dy[i]
            if new_x < 0 or new_x>=N or new_y < 0 or new_y >= N:
                continue
            if board[new_x][new_y] == 1:
                continue
            if d == -1:
                new_cost = cost+100
            elif d%2 == i%2:
                new_cost = cost+100
            else:
                new_cost = cost + 600
            if (new_x,new_y) not in visited or visited[(new_x,new_y)] >= new_cost:
                visited[(new_x,new_y)] = new_cost
                queue.append((new_x,new_y,new_cost,i))
    return answer