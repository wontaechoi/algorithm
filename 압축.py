def solution(msg):
    dic = {}
    i = 1
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        dic[c] = i
        i += 1
    index = 0
    answer = []
    while index < len(msg):
        for i in range(len(msg), index, -1):
            mes = msg[index:i]
            if mes in dic:
                answer.append(dic[mes])
                if i != len(msg):
                    dic[msg[index:i + 1]] = max(dic.values()) + 1
                index = i
                break

    return answer