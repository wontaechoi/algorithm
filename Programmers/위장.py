#https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    clothes_hash = {}
    for c in clothes:
        if c[1] not in clothes_hash:
            clothes_hash[c[1]] = []
        clothes_hash[c[1]].append(c[0])
    total = 1

    for c in clothes_hash:
        total *= (len(clothes_hash[c]) + 1)

    answer = total - 1
    return answer