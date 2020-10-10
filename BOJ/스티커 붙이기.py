def turn90(actual_sticker):
    r, c = len(actual_sticker), len(actual_sticker[0])
    new_sticker = [[0 for _ in range(r)] for __ in range(c)]
    new_loc = []
    for i in range(c):
        for j in range(r-1, -1, -1):
            new_sticker[i][r - j - 1] = actual_sticker[j][i]
            if new_sticker[i][r - j - 1] == 1:
                new_loc.append((i,r-j-1))

    return new_sticker, new_loc

def attach(sticker, actual_sticker, notebook):
    global N, M, K
    for turn in range(4):
        r, c = len(actual_sticker), len(actual_sticker[0])
        for i in range(N - r + 1):
            for j in range(M - c + 1):
                flag = False
                for dx, dy in sticker:
                    if notebook[i + dx][j + dy] == 1:
                        flag = True
                        break
                if flag:
                    continue
                for dx, dy in sticker:
                    notebook[i + dx][j + dy] = 1
                return notebook, True
        actual_sticker, sticker = turn90(actual_sticker)
    return notebook, False





def sol(stickers, actual_stickers, notebook):
    global N, M, K
    for k in range(K):
        sticker = stickers[k]
        actual_sticker = actual_stickers[k]

        notebook, attached = attach(sticker, actual_sticker, notebook)
    count = 0
    for i in range(N):
        for j in range(M):
            if notebook[i][j] == 1:
                count += 1

    return count






N, M, K = map(int, input().split())
stickers = []
actual_stickers = []
for k in range(K):
    r, c = map(int, input().split())
    sticker = []
    actual_sticker = []
    for i in range(r):
        row = list(map(int, input().split()))
        for j in range(c):
            if row[j] == 1:
                sticker.append((i, j))
        actual_sticker.append(row)
    stickers.append(sticker)
    actual_stickers.append(actual_sticker)

notebook = [[0 for _ in range(M)] for __ in range(N)]

count = sol(stickers, actual_stickers, notebook)
print(count)