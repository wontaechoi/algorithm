def sol(way, up, down, front, back, left, right):
    part, clock = way[0], way[1]


    if part == 'U':
        temp = front[0].copy()
        if clock == '+':
            up = turn90(up)
            front[0] = right[0]
            right[0] = back[0]
            back[0] = left[0]
            left[0] = temp

        else:
            up = counterclock(up)
            front[0] = left[0]
            left[0] = back[0]
            back[0] = right[0]
            right[0] = temp

    elif part == 'D':
        temp = front[2].copy()
        if clock == '+':
            down = turn90(down)
            front[2] = left[2]
            left[2] = back[2]
            back[2] = right[2]
            right[2] = temp
        else:
            down = counterclock((down))
            front[2] = right[2]
            right[2] = back[2]
            back[2] = left[2]
            left[2] = temp

    elif part == 'F':
        temp = up[2].copy()
        if clock == '+':
            front = turn90(front)
            for i in range(3):
                up[2][i] = left[2-i][2]
            for i in range(3):
                left[i][2] = down[2][2-i]
            for i in range(3):
                down[2][i] = right[i][0]
            for i in range(3):
                right[i][0] = temp[i]
        else:
            front = counterclock(front)
            for i in range(3):
                up[2][i] = right[i][0]
            for i in range(3):
                right[i][0] = down[2][i]
            for i in range(3):
                down[2][i] = left[2-i][2]
            for i in range(3):
                left[i][2] = temp[2-i]

    elif part == 'B':
        temp = up[0].copy()
        if clock == '+':
            back = turn90(back)
            for i in range(3):
                up[0][i] = right[i][2]
            for i in range(3):
                right[i][2] = down[0][i]
            for i in range(3):
                down[0][i] = left[2-i][0]
            for i in range(3):
                left[i][0] = temp[2-i]
        else:
            back = counterclock(back)
            for i in range(3):
                up[0][i] = left[2-i][0]
            for i in range(3):
                left[i][0] = down[0][2-i]
            for i in range(3):
                down[0][i] = right[i][2]
            for i in range(3):
                right[i][2] = temp[i]

    elif part == 'L':
        temp = [up[i][0] for i in range(3)]
        if clock == '+':
            left = turn90(left)
            for i in range(3):
                up[i][0] = back[2-i][2]
            for i in range(3):
                back[i][2] = down[i][2]
            for i in range(3):
                down[i][2] = front[2-i][0]
            for i in range(3):
                front[i][0] = temp[i]
        else:
            left = counterclock(left)
            for i in range(3):
                up[i][0] = front[i][0]
            for i in range(3):
                front[i][0] = down[2-i][2]
            for i in range(3):
                down[i][2] = back[i][2]
            for i in range(3):
                back[i][2] = temp[2-i]
    elif part == 'R':
        temp = [up[i][2] for i in range(3)]
        if clock == '+':
            right = turn90(right)
            for i in range(3):
                up[i][2] = front[i][2]
            for i in range(3):
                front[i][2] = down[2 - i][0]
            for i in range(3):
                down[i][0] = back[i][0]
            for i in range(3):
                back[i][0] = temp[2 - i]
        else:
            right = counterclock(right)
            for i in range(3):
                up[i][2] = back[2 - i][0]
            for i in range(3):
                back[i][0] = down[i][0]
            for i in range(3):
                down[i][0] = front[2 - i][2]
            for i in range(3):
                front[i][2] = temp[i]




    return up,down,front,back,left,right

def turn90(area):
    temp = [['' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[i][j] = area[2-j][i]
    return temp

def counterclock(area):
    temp = [['' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[i][j] = area[j][2-i]
    return temp

T = int(input())
for i in range(T):
    up = [['w','w','w'],['w','w','w'],['w','w','w']]
    down = [['y','y','y'],['y','y','y'],['y','y','y']]
    front = [['r','r','r'],['r','r','r'],['r','r','r']]
    back = [['o','o','o'],['o','o','o'],['o','o','o']]
    left = [['g','g','g'],['g','g','g'],['g','g','g']]
    right = [['b','b','b'],['b','b','b'],['b','b','b']]

    board = [up,down,front,back,left,right]
    n = int(input())
    if n != 1:
        ways = list(map(str, input().split()))
    else:
        ways = [input()]
    for way in ways:
        up,down,front,back,left,right = sol(way, up,down,front,back,left,right)

    for i in range(3):
        temp = ''
        for j in range(3):
            temp += up[i][j]
        print(temp)
