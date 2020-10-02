def solve(d1,d2,x,y):
    global N, city
    new_city = [[0 for _ in range(N)] for __ in range(N)]

    for i in range(x+d1):
        for j in range(y+1):

            new_city[i][j] = 1

    for i in range(x+d2+1):
        for j in range(y+1, N):
            new_city[i][j] = 2

    for i in range(x+d1, N):
        for j in range(y-d1+d2):
            new_city[i][j] = 3

    for i in range(x+d2+1, N):
        for j in range(y-d1+d2, N):
            new_city[i][j] = 4
    dic = {}
    for i in range(d1 + 1):
        new_city[x+i][y-i] = 5
        if x+i not in dic:
            dic[x+i] = set()
        dic[x + i].add(y - i)
        new_city[x + d2 + i][y + d2 - i] = 5
        if x+d2+i not in dic:
            dic[x+d2+i] = set()
        dic[x+d2+i].add(y + d2 - i)

    for i in range(d2 + 1):
        new_city[x+i][y+i] = 5
        if x+i not in dic:
            dic[x+i] = set()
        dic[x+i].add(y+i)
        new_city[x+d1+i][y-d1+i] = 5
        if x+d1+i not in dic:
            dic[x+d1+i] = set()
        dic[x+d1+i].add(y-d1+i)

    for x in dic.keys():
        if len(dic[x]) > 1:
            l = sorted(list(dic[x]))
            for y in range(l[0]+1, l[1]):
                new_city[x][y] =5

    return new_city


def calc(new_city):
    global N, city
    dic = {}
    for i in range(1, 6):
        dic[i] = 0

    for x in range(N):
        for y in range(N):
            dic[new_city[x][y]] += city[x][y]

    max_p = max(list(dic.values()))
    min_p = min(list(dic.values()))

    return max_p - min_p
N = int(input())
city = []
for i in range(N):
    city.append(list(map(int,input().split())))


answer = float('inf')
for d1 in range(1, N-1):
    for d2 in range(1, N-1):
        if d1 + d2 < N - 1:
            for x in range(N-d1-d2):
                for y in range(1 + d1, N-d2):
                    new_city = solve(d1,d2,x,y)
                    answer = min(calc(new_city), answer)
print(answer)