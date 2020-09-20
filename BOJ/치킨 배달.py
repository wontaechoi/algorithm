def combinations(array, n):
    def combi(arr,n):
        if len(arr) == n:
            temp = arr.copy()
            all_coms.append(temp)
            return

        start = array.index(arr[-1]) +1 if arr else 0
        for i in range(start, len(array)):
            arr.append(array[i])
            combi(arr, n)
            arr.pop()
    combi([],n)


N, M = map(int, input().split())
houses = []
chickens = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            houses.append((i,j))
        elif row[j] == 2:
            chickens.append((i,j))

all_coms = []
combinations([i for i in range(len(chickens))], M)
answer = float('inf')
for com in all_coms:
    summ = 0
    for house in houses:
        min_dis = float('inf')
        h_x, h_y = house
        for chick in com:
            x, y = chickens[chick]
            min_dis = min(min_dis, abs(h_x - x) + abs(h_y - y))
        summ += min_dis
    answer = min(answer, summ)
print(answer)