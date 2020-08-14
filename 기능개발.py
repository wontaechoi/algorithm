import math


def solution(progresses, speeds):
    times = [math.ceil((100 - i) / j) for i, j in zip(progresses, speeds)]
    answer = []
    prev = times[0]
    count = 1
    for i in range(1, len(times)):
        if times[i] > prev:
            answer.append(count)
            prev = times[i]
            count = 1
        else:
            count += 1
    answer.append(count)

    return answer