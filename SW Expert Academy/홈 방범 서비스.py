T= int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    houses = []
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 1:
                houses.append((i,j))
    answer = 0
    for K in range(1,N+2):
        cost = K*K + (K-1)*(K-1)
        for i in range(N):
            for j in range(N):
                count = 0
                for x,y in houses:
                    if abs(i-x) + abs(j-y) < K:
                        count += 1
                profit = count * M

                if profit >= cost:
                    answer = max(count, answer)
    print("#{} {}".format(test_case, answer))
