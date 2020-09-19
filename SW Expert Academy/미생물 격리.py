dx = [-1,1,0,0]
dy = [0,0,-1,1]


def sol(N, organisms):
    dic = {}
    for i, (x,y,c,d) in enumerate(organisms):
        new_x = x + dx[d]
        new_y = y + dy[d]
        new_c = c
        new_d = d
        if new_x == 0 or new_y ==0 or new_x == N-1 or new_y == N-1:
            new_d = d + 1 if d % 2 ==0 else d - 1
            new_c = c //2
            
        if new_c > 0:
            if (new_x,new_y) not in dic:
                dic[(new_x,new_y)] = (new_c, new_d, new_c)
            else:
                all_c, compare_d, compare_c = dic[(new_x, new_y)]
                if compare_c > new_c:
                    dic[(new_x,new_y)] = (all_c + new_c, compare_d, compare_c)
                else:
                    dic[(new_x, new_y)] = (all_c + new_c, new_d, new_c)
    new = []
    for (x,y) in dic.keys():
        new.append((x, y, dic[(x, y)][0], dic[(x, y)][1]))
    return new

T = int(input())
for test_case in range(1, T+1):

    N, M, K = map(int, input().split())
    organisms = []
    for i in range(K):
        x,y, c, d = map(int, input().split())
        organisms.append((x,y,c,d-1))

    for i in range(M):
        organisms = sol(N, organisms)
    answer = 0
    for x,y,c,d in organisms:
        answer += c
    print("#{} {}".format(test_case, answer))