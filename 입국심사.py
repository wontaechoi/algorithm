def solution(n, times):
    answer = max(times)*n
    left = 0
    right = answer
    while left <= right:
        mid = (left+right)//2
        dealed = 0
        for time in times:
            dealed += mid//time
        if dealed >= n:
            answer = min(answer, mid)
            right = mid -1
        else:
            left = mid +1
    return answer