from itertools import product


def calculate_score(x1, y1):
    global N, M, C, area
    honey = area[x1][y1:y1+M]
    score = 0
    def calculate(honey, index, c, point):
        nonlocal score
        if c - honey[index] < 0:
            score = max(score, point)
            return
        if index + 1 == len(honey):
            score = max(score, point + honey[index] ** 2)
            return
        calculate(honey, index + 1, c, point)
        calculate(honey, index + 1, c - honey[index], point + honey[index] ** 2)
        return

    calculate(honey, 0, C, 0)
    return score
T = int(input())
for test_case in range(1, T+1):
    N, M, C = map(int, input().split())
    area = []
    for i in range(N):
        area.append(list(map(int, input().split())))

    possible = list(product(*[[i for i in range(N)],[i for i in range(N-M + 1)]]))
    answer = 0
    for i in range(len(possible) -1):
        x1, y1 = possible[i]
        for j in range(1, len(possible)):
            if i != j:
                x2, y2 = possible[j]
                if (x1 == x2 and y2 >= y1 + M) or (x1 != x2):
                    score = calculate_score(x1,y1) + calculate_score(x2,y2)
                    answer = max(answer, score)
    print("#{} {} ".format(test_case, answer))