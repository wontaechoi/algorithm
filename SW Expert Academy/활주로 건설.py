"""6 2
3 3 3 2 1 1
3 3 3 2 2 1
3 3 3 3 3 2
2 2 3 2 2 2
2 2 3 2 2 2
2 2 2 2 2 2"""
def sol(N,X, row):
    flag = True
    visited = []
    former = row[0]
    for i in range(N-1):
        if abs(row[i+1] - row[i]) > 1:
            return False
        elif row[i] == row[i + 1] - 1:
            prev = row[i]
            for j in range(i - X+1, i+1):
                if j < 0 or j >= N:
                    return False

                if row[j] != prev or j in visited:
                    return False
                visited.append(j)
        elif row[i] == row[i + 1] + 1:
            prev = row[i+1]
            for j in range(i + 1, i + X+1):
                if j < 0 or j >= N:
                    return False
                if row[j] != prev or j in visited:
                    return False
                visited.append(j)
    return True


for test_case in range(1, int(input())+1):
    N, X = map(int, input().split())
    board1 = []
    board2 = [[] for i in range(N)]
    for i in range(N):
        row = list(map(int,input().split()))
        board1.append(row)
        for j in range(N):
            board2[j].append(row[j])
    board = board1 + board2
    answer = 0
    for row in board:
        if sol(N,X,row):
            answer+=1
    print("#{} {}".format(test_case, answer))