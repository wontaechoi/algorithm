def play(order):
    global N, results
    score = 0
    index = 0
    for inning in range(N):
        out = 0
        b1, b2, b3 = 0,0,0
        while out < 3:
            if results[inning][order[index]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif results[inning][order[index]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0,1,b1
            elif results[inning][order[index]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0,0,1
            elif results[inning][order[index]] == 4:
                score += (1 + b1 + b2 + b3)
                b1, b2, b3 = 0,0,0
            else:
                out += 1
            index = index + 1 if index < 8 else 0
    return score

import sys
from itertools import permutations

N = int(sys.stdin.readline())
results = []
for i in range(N):
    results.append(list(map(int, sys.stdin.readline().split())))

orders = list(permutations([i for i in range(1, 9)], 8))
answer = 0
for order in orders:
    order = list(order)[:3] + [0] + list(order)[3:]
    answer = max(answer, play(order))
print(answer)