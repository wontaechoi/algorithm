def drop_green(t, y, green, ind):
    if t == 1:
        found = False
        index = 5
        for i in range(6):
            if green[i][y] != 0:
                found = True
                index = i - 1
                break
        if not found:
            green[5][y] = (t, ind)
        else:
            green[index][y] = (t, ind)
    elif t == 3:
        found = False
        index = 5
        for i in range(6):
            if green[i][y] != 0:
                found = True
                index = i - 1
                break
        if not found:
            green[5][y] = (t, ind)
            green[4][y] = (t, ind)
        else:
            green[index][y] = (t, ind)
            green[index-1][y] = (t, ind)

    else:
        found = False
        index = 5
        for i in range(6):
            if green[i][y] != 0 or green[i][y+1] != 0:
                found = True
                index = i - 1
                break
        if not found:
            green[5][y] = (t, ind)
            green[5][y+1] = (t, ind)
        else:
            green[index][y] = (t, ind)
            green[index][y+1] = (t, ind)
    return green

def drop_blue(t, x,  blue, ind):
    x = 3 - x
    if t == 1:
        found = False
        index = 5
        for i in range(6):
            if blue[i][x] != 0:
                found = True
                index = i - 1
                break
        if not found:
            blue[5][x] = (t, ind)
        else:
            blue[index][x] = (t, ind)

    elif t == 2:
        found = False
        index = 5
        for i in range(6):
            if blue[i][x] != 0:
                found = True
                index = i - 1
                break
        if not found:
            blue[5][x] = (t, ind)
            blue[4][x] = (t, ind)
        else:
            blue[index][x] = (t, ind)
            blue[index - 1][x] = (t, ind)

    else:
        found = False
        index = 5
        for i in range(6):
            if blue[i][x] != 0 or blue[i][x - 1] != 0:
                found = True
                index = i - 1
                break
        if not found:
            blue[5][x] = (t, ind)
            blue[5][x - 1] = (t, ind)
        else:
            blue[index][x] = (t, ind)
            blue[index][x - 1] = (t, ind)
    return blue

def check_filled(array):
    new_array = []
    point = 0
    for arr in array:
        if 0 in arr:
            new_array.append(arr)
        else:
            new_array.append([0 for _ in range(4)])
            point += 1

    return new_array, point

def check_section(array):
    count = 0
    for i in range(2):
        for j in range(4):
            if array[i][j] != 0:
                count += 1
                break
    if count == 0:
        return array
    else:
        new = [[0 for _ in range(4)] for _ in range(count)] + array[:-count]
        return new

def check_drop_green(green):
    dic = {}
    for i in range(5, -1, -1):
        for j in range(4):
            if green[i][j] != 0:
                if green[i][j] not in dic:
                    dic[green[i][j]] = []
                dic[green[i][j]].append((i,j))
    for point in dic.keys():
        dic[point].sort(key = lambda x: -x[0])
        if len(dic[point]) == 1:
            x, y = dic[point][0]
            green[x][y] = 0
            while x< 6 and green[x][y] == 0:
                x += 1
            green[x-1][y] = point
        else:
            if point[0] == 3:
                x, y = dic[point][0]
                green[x][y] = 0
                green[x-1][y] = 0
                while x < 6 and green[x][y] == 0:
                    x += 1
                green[x-1][y] = point
                green[x-2][y] = point
            else:
                x, y = dic[point][0]
                green[x][y] = 0
                green[x][y+1] = 0
                while x < 6 and green[x][y] == 0 and green[x][y+1] == 0:
                    x += 1
                green[x-1][y] = point
                green[x-1][y+1] = point

    return green

def check_drop_blue(blue):
    dic = {}
    for i in range(5, -1, -1):
        for j in range(4):
            if blue[i][j] != 0:
                if blue[i][j] not in dic:
                    dic[blue[i][j]] = []
                dic[blue[i][j]].append((i,j))
    for point in dic.keys():
        dic[point].sort(key = lambda x: -x[0])
        if len(dic[point]) == 1:
            x, y = dic[point][0]
            blue[x][y] = 0
            while x< 6 and blue[x][y] == 0:
                x += 1
            blue[x-1][y] = point
        else:
            if point[0] == 2:
                x, y = dic[point][0]
                blue[x][y] = 0
                blue[x-1][y] = 0
                while x < 6 and blue[x][y] == 0:
                    x += 1
                blue[x-1][y] = point
                blue[x-2][y] = point
            else:
                x, y = dic[point][0]
                blue[x][y] = 0
                blue[x][y+1] = 0
                while x < 6 and blue[x][y] == 0 and blue[x][y+1] == 0:
                    x += 1
                blue[x-1][y] = point
                blue[x-1][y+1] = point

    return blue








N = int(input())
orders = []
for i in range(N):
    t, x, y = map(int ,input().split())
    orders.append((t, x,y))

green = [[0 for i in range(4)] for j in range(6)]
blue = [[0 for i in range(4)] for j in range(6)]

score = 0
for i, (t, x,y )in enumerate(orders):
    green = drop_green(t,y,green, i)
    while True:
        green, point = check_filled(green)
        if point == 0:
            break
        green = check_drop_green(green)
        score += point
    green = check_section(green)

    blue = drop_blue(t,x,blue, i)
    while True:
        blue, point = check_filled(blue)
        if point == 0:
            break
        blue = check_drop_blue(blue)
        score += point
    blue = check_section(blue)

print(score)
count = 0
for i in range(6):
    for j in range(4):
        if green[i][j] != 0:
            count += 1
        if blue[i][j] != 0:
            count += 1

print(count)

