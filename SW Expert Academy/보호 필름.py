from itertools import combinations
def combination(array, n):
    def combin(arr,n):
        if len(arr) == n:
            temp = arr.copy()
            combi.append(temp)
            return

        start = array.index(arr[-1]) + 1 if arr else 0
        for i in range(start, len(array)):
            combin(arr + [array[i]], n)
    combin([],n)
    return
def permutation(array, n):
    def perm(arr,n):
        if len(arr) == n:
            temp = arr.copy()
            med.append(temp)
            return

        for i in range(len(array)):
            perm(arr + [array[i]], n)
    perm([],n)
    return

def put_med(com, medic, films):
    new_films = films.copy()
    for i in range(len(com)):
        new_films[com[i]] = [medic[i]] * len(new_films[com[i]])
    return new_films

def check(films, K):
    d = len(films)
    for j in range(len(films[0])):
        prev = -1
        found = False
        count = 0
        for i in range(d):
            if films[i][j] == prev:
                count += 1
                if count == K:
                    found = True
                    break
            else:
                count = 1
                prev = films[i][j]
        if not found:
            return False
    return True
T = int(input())
for test_case in range(1, T+1):
    D, W, K = map(int, input().split())
    films = []
    for i in range(D):
        row = list(map(int, input().split()))
        films.append(row)

    combi = []
    for n in range(D +1):
        combination([i for i in range(D)], n)
    answer = float('inf')
    if K == 1:
        answer = 0
    else:
        for com in combi:
            med = []
            permutation([0,1], len(com))
            if com:
                for medic in med:
                    new_films = put_med(com, medic, films)
                    ans = check(new_films, K)
                    if ans:
                        break
            else:
                ans = check(films,K)
            if ans:
                answer = len(com)
                break
    print("#{} {}".format(test_case, answer))
