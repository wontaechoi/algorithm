def solution(citations):
    citations.sort()
    answer = len(citations)
    for i, cit in enumerate(citations):
        if cit >= len(citations) - i:
            break
        answer -= 1

    return answer