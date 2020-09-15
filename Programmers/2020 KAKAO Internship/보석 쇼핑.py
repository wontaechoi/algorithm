def solution(gems):
    answer = [0, len(gems)]
    left = 0
    right = 0
    N = len(gems)
    gems_set = list(set(gems))
    gems_dict = {gems[left]: 1}
    while left < N and right < N:
        if len(gems_set) != len(gems_dict):
            right += 1
            if right == N:
                break
            if gems[right] not in gems_dict:
                gems_dict[gems[right]] = 0
            gems_dict[gems[right]] += 1
        else:
            if answer[1] - answer[0] > right - left:
                answer = [left + 1, right + 1]
            gems_dict[gems[left]] -= 1
            if gems_dict[gems[left]] == 0:
                del gems_dict[gems[left]]
            left += 1

    return answer