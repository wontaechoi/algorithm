def do_R(array, N, M):
    new_array = []
    for i in range(N):
        dic = {}
        row = []
        for j in range(M):
            if array[i][j] != 0:
                if array[i][j] not in dic:
                    dic[array[i][j]] = 0
                dic[array[i][j]] += 1
        temp = []
        for n in dic.keys():
            temp.append((n,dic[n]))
        temp.sort(key = lambda x : [x[1],x[0]])
        for x, y in temp:
            row += [x,y]
        new_array.append(row)
    max_len = 0
    for row in new_array:
        max_len = max(max_len, len(row))
    for i, row in enumerate(new_array):
        if len(row) < max_len:
            new_array[i] += [0] * (max_len - len(row))


    return new_array

def do_C(array, N, M):
    temp_array = []
    for j in range(M):
        temp_row = []
        for i in range(N):
            temp_row.append(array[i][j])
        temp_array.append(temp_row)
    new_array = []
    for i in range(M):
        dic = {}
        row = []
        for j in range(N):
            if temp_array[i][j] != 0:
                if temp_array[i][j] not in dic:
                    dic[temp_array[i][j]] = 0
                dic[temp_array[i][j]] += 1
        temp = []
        for n in dic.keys():
            temp.append((n, dic[n]))
        temp.sort(key=lambda x: [x[1], x[0]])
        for x, y in temp:
            row += [x, y]
        new_array.append(row)
    max_len = 0
    for row in new_array:
        max_len = max(max_len, len(row))
    for i, row in enumerate(new_array):
        if len(row) < max_len:
            new_array[i] += [0] * (max_len - len(row))
    return_array = []

    for j in range(len(new_array[0])):
        temp_row = []
        for i in range(len(new_array)):
            temp_row.append(new_array[i][j])
        return_array.append(temp_row)
    return return_array


def convert(array):
    N, M  = len(array), len(array[0])
    if N >= M:
        array = do_R(array, N, M)
    else:
        array = do_C(array, N, M)
    for i, row in enumerate(array):
        if len(row) > 100:
            array[i] = row[:100]
    return array


r, c, k = map(int, input().split())
r -= 1
c -= 1
A = []
for i in range(3):
    A.append((list(map(int, input().split()))))
answer = 0
while True:
    if len(A) > r and len(A[0]) > c:
        if A[r][c] == k:
            break
    if answer > 100:
        answer = -1
        break
    A = convert(A)
    answer += 1
print(answer)