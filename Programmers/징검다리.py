def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance
    rocks.append(distance)
    rocks.sort()
    while left <=right:
        mid = (left+right)//2
        prev = 0
        count = 0
        ans = distance
        for i in range(len(rocks)):
            if rocks[i]-prev  < mid:
                count +=1
            else:
                ans = min(ans, rocks[i]-prev)
                prev = rocks[i]
        if count > n:
            right = mid -1
        else:
            left = mid + 1
            answer = ans
    print(ans)
    return answer