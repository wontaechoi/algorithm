import re


def solution(s):
    dic = {}

    tup = re.split(r'[{},]', s)
    for x in tup:
        if x.isnumeric():
            if x not in dic:
                dic[x] = 0
            dic[x] += 1
    tups = []
    for x in dic.keys():
        tups.append((x, dic[x]))
    tups.sort(key=lambda x: [-x[1], x[0]])
    answer = []
    for x, y in tups:
        answer.append(int(x))
    return answer