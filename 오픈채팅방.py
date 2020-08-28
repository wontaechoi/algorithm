def solution(record):
    answer = []
    dic = {}
    move = []
    for r in record:
        word = list(r.split())
        if word[0] == 'Enter':
            dic[word[1]] = word[2]
            move.append(('Enter', word[1]))
        elif word[0] =='Change':
            dic[word[1]] = word[2]
        else:
            move.append(('Leave', word[1]))
    for m, uid in move:
        if m == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(dic[uid]))
        else:
            answer.append('{}님이 나갔습니다.'.format(dic[uid]))
    return answer