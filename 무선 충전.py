T= int(input())
for test_case in range(1, T+1):
    dx = [0, 0, 1,0,-1]
    dy = [0, -1,0,1,0]
    M, A = map(int, input().split())
    move_a = list(map(int,input().split()))
    move_b = list(map(int,input().split()))
    batteries = []
    for a in range(A):
        x,y, c, p = map(int, input().split())
        batteries.append((x,y,c,p))
    pos_a = (1,1)
    pos_b = (10, 10)

    score = 0
    for t in range(M+1):
        x_a, y_a = pos_a
        x_b, y_b = pos_b
        b_a = []
        b_b = []
        for i, battery in enumerate(batteries):
            x,y,c,p = battery
            count = 0
            if abs(x_a -x) + abs(y_a - y) <= c:
                b_a.append(i)
            if abs(x_b -x) + abs(y_b - y) <= c:
                b_b.append(i)
        if not b_a and b_b:
            m_b = 0
            for b in b_b:
                m_b = max(m_b, batteries[b][3])
            score += m_b
        elif b_a and not b_b:
            m_b = 0
            for b in b_a:
                m_b = max(m_b, batteries[b][3])
            score += m_b
        elif b_a and b_b:
            m_b= 0
            for i in b_a:
                for j in b_b:
                    if i == j:
                        m_b = max(m_b, batteries[i][3])
                    else:
                        m_b = max(m_b,batteries[i][3] + batteries[j][3])
            score += m_b

        x_a, y_a = pos_a
        x_b, y_b = pos_b
        if t < M:
            pos_a = (x_a + dx[move_a[t]], y_a + dy[move_a[t]])
            pos_b = (x_b + dx[move_b[t]], y_b + dy[move_b[t]])


    print("#{} {}".format(test_case,score))