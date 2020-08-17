def solution(priorities, location):
    index = [i for i in range(len(priorities))]
    answer_ind = [-1 for i in range(len(priorities))]
    count = 0
    while priorities:
        current = priorities.pop(0)
        i = index.pop(0)
        flag = False
        for pr in priorities:
            if current < pr:
                flag = True
                break
        if flag:
            priorities.append(current)
            index.append(i)
        else:
            answer_ind[i] = count
            count +=1
    return answer_ind[location] +1