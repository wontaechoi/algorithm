test_case = int(input())
for t in range(1, test_case + 1):
    N, K = map(int, input().split())
    m = N // 4
    line = input()
    possible = []
    for i in range(m):
        for i in range(0, len(line), m):
            if line[i:i+m] not in possible:
                possible.append(line[i:i+m])
        line = line[-1] + line[:-1]
    numbers = []
    for pos in possible:
        numbers.append(int(pos, 16))
    print("#{} {}".format(t, sorted(numbers, reverse= True)[K-1]))