from itertools import permutations
def solution(n, weak, dist):
    answer = len(dist) +1
    to_clean = len(weak)
    weak = weak + [i +n for i in weak]
    order_list = list(permutations([_ for _ in range(len(dist))]))
    for i, start_point in enumerate(weak[:-to_clean]):
        for order in order_list:
            count = 0
            index = i
            for d in list(order):
                count +=1
                helped = dist[d] + weak[index]
                if helped >= weak[i+to_clean-1]:
                    answer = min(answer, count)
                    break
                for q in range(i, i+to_clean):
                    if weak[q]> helped:
                        index = q
                        break
    if answer > len(dist):
        answer = -1
    return answer