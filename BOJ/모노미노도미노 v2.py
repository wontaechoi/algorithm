def put_block(index, order, color, array):
    if color == 0:
        x, y, t = order
    elif color == 1:
        x, y, t = order
        if t == 1:
            y = 4 - x - 1
        elif t == 2:
            t = 3
            y = 4 - x - 1
        elif t == 3:
            t = 2
            y = 3 - x - 1
    if t == 1:
        check_x = 1
        while check_x + 1 < 6 and array[check_x + 1][y] == 0:
            check_x += 1
        array[check_x][y] = (index, t)
    elif t == 2:
        check_x = 1
        while check_x + 1 < 6 and array[check_x + 1][y] == 0 and array[check_x + 1][y + 1] == 0:
            check_x += 1
        array[check_x][y] = (index, t)
        array[check_x][y + 1] = (index, t)
    else:
        check_x = 1
        while check_x + 1 < 6 and array[check_x + 1][y] == 0:
            check_x += 1
        array[check_x][y] = (index, t)
        array[check_x - 1][y] = (index, t)

    return array




def check_full(array):
    new_array = []
    point = 0
    for i in range(6):
        if 0 in array[i]:
            new_array.append(array[i])
        else:
            point += 1
    return new_array, point

def drop(array):
    dic = {}
    for i in range(len(array)- 1, -1, -1):
        for j in range(4):
            if array[i][j] != 0:
                if array[i][j] not in dic :
                    dic[array[i][j]] = []
                dic[array[i][j]].append((i, j))

    for point in dic.keys():
        index, t = point
        dic[(index, t)].sort(key = lambda x: [-x[0], x[1]])
        if len(dic[(index, t)]) == 1:
            x, y = dic[point][0]
            array[x][y] = 0
            while x < len(array) and array[x][y] == 0:
                x += 1
            array[x - 1][y] = point
        else:
            if t == 3:
                x, y = dic[point][0]
                array[x][y] = 0
                array[x - 1][y] = 0
                while x < len(array) and array[x][y] == 0:
                    x += 1
                array[x - 1][y] = point
                array[x - 2][y] = point

            else:
                x, y = dic[point][0]
                array[x][y] = 0
                array[x][y + 1] = 0
                while x < len(array) and array[x][y] == 0 and array[x][y + 1] == 0:
                    x += 1
                array[x - 1][y] = point
                array[x - 1][y + 1] = point




    return [[0,0,0,0] for _ in range(6 - len(array))] + array

def check_invade(array):
    count = 0
    for i in range(2):
        for j in range(4):
            if array[i][j] != 0:
                count += 1
                break
    if count == 0:
        return array
    return [[0, 0, 0, 0] for _ in range(count)] + array[:len(array)-count]

def count(array):
    c = 0
    for i in range(6):
        for j in range(4):
            if array[i][j] != 0:
                c += 1
    return c

green = [[0 for _ in range(4)] for __ in range(6)]
blue = [[0 for _ in range(4)] for __ in range(6)]
N = int(input())
orders = []
for i in range(N):
    t, x, y = map(int, input().split())
    orders.append((x, y, t))

answer = 0
for index, order in enumerate(orders):
    green = put_block(index, order, 0, green)
    temp, point = check_full(green)
    while point != 0:
        answer += point
        temp = drop(temp)
        temp, point = check_full(temp)
    green = check_invade(temp)

    blue = put_block(index, order, 1, blue)

    temp, point = check_full(blue)
    while point != 0:
        answer += point
        temp = drop(temp)
        temp, point = check_full(temp)
    blue = check_invade(temp)



c = count(green) + count(blue)

print(answer)
print(c)
