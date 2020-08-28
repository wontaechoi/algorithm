def solution(food_times, k):
    N = len(food_times)
    foods = [(food_times[i], i + 1) for i in range(N)]
    foods.sort(key=lambda x: x[0])
    delete = 0
    prev = delete
    prev_food = 0
    if sum(food_times) <= k:
        return -1
    for i, food in enumerate(foods):
        prev = delete
        delete += (food[0] - prev_food) * (N - i)
        prev_food = food[0]
        if delete > k:
            break
    left = sorted(foods[i:], key=lambda x: x[1])
    answer = left[(k - prev) % len(left)][1]

    return answer