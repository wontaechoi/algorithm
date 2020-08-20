def solution(brown, yellow):
    for n in range(1, int(yellow//2) + 1):
        if yellow % n == 0:
            w = yellow//n
            if 2 * n + 2 * w + 4 == brown:
                return [2 + w, n+2]
    return [3,3]