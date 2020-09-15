def solution(stones, k):
    stones = stones
    answer = max(stones)
    left = 0
    right = max(stones)
    while left <= right:
        mid = (left + right) // 2
        flag = False
        count = 0
        for i in range(len(stones)):
            if stones[i] <= mid:
                count += 1


            else:
                count = 0
            if count >= k:
                flag = True
                break
        if flag:
            right = mid - 1
        else:
            left = mid + 1

    return left