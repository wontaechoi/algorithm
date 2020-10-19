def move(belt, people):
    global N
    belt = [belt[-1]] + belt[:-1]

    new_people = []
    for i, index in enumerate(people):
        index += 1
        if index != N - 1:
            if belt[index + 1] != 0 and index + 1 not in new_people:
                if index + 1 != N - 1:
                    new_people.append(index + 1)
                belt[index+1] = belt[index+1] - 1
            else:
                new_people.append(index)

    if belt[0] != 0:
        new_people.append(0)
        belt[0] -= 1

    return belt, new_people

N, K = map(int,input().split())
belt = list(map(int,input().split()))

time = 0
people = []
while True:
    belt, people = move(belt, people)
    time += 1
    count =0
    for i in belt:
        if i == 0:
            count += 1
            if count == K:
                break
    if count == K:
        break
print(time)