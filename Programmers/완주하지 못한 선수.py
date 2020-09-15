#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    par_dict = {}
    for part in participant:
        if part not in par_dict:
            par_dict[part] = 1
        else:
            par_dict[part] += 1
    for com in completion:
        par_dict[com] -= 1
    answer = ''
    for par in par_dict.keys():
        if par_dict[par] != 0:
            answer = par
    return answer