from itertools import combinations

def count(time,stair_time):
    in_stairs = []
    t = 0
    time.sort()
    while in_stairs or time:
        new = []
        for n in range(len(in_stairs)):
            if in_stairs[n] < stair_time:
                new.append(in_stairs[n] + 1)
        in_stairs = new
        new = []
        for n in range(len(time)):
            if time[n] <= 0 and len(in_stairs) < 3:
                in_stairs.append(1)
            else:
                new.append(time[n] - 1)
        time = new
        t += 1
    return t

def sol(to_one, to_two, stairs):
    one_time = []
    two_time = []
    stair1_time = stairs[0][2]
    stair2_time = stairs[1][2]
    ans1 = 0
    ans2 = 0
    if to_one:
        for x,y in to_one:
            time = abs(stairs[0][0] - x) + abs(stairs[0][1]-y)
            one_time.append(time)
        ans1 = count(one_time, stair1_time)
    if to_two:
        for x,y in to_two:
            time = abs(stairs[1][0] - x) + abs(stairs[1][1] - y)
            two_time.append(time)
        ans2 = count(two_time, stair2_time)
    return max(ans1, ans2)

T= int(input())
for test_case in range(1, T+1):
    N = int(input())
    people = []
    stairs = []
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 1:
                people.append((i,j))
            elif row[j] >=2:
                stairs.append((i,j,row[j]))
    combi = []
    answer = float('inf')
    if len(people) == 1:
        combi = [people[0]]
        x = sol([people[0]], [], stairs)
        if x < answer:
            answer = min(answer, x)
        x = sol([], [people[0]], stairs)
        if x < answer:
            answer = min(answer, x)

    else:
        for i in range(len(people) + 1):
            c = list(combinations(people, i))
            t = []
            for x in c:
                t.append(list(x))
            combi += t


        for c in combi:
            to_one = c
            to_two = list(set(people) - set(c))
            x = sol(to_one, to_two, stairs)
            if x < answer:
                answer = min(answer, x)
    print("#{} {}".format(test_case,answer))
