def solution(numbers, hand):
    dic = {}
    buttons = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#']
    index = 0
    for i in range(4):
        for j in range(3):
            dic[buttons[index]] = (i, j)
            index += 1
    l = dic['*']
    r = dic['#']
    answer = ''
    for number in numbers:
        if number in [1, 4, 7]:
            l = dic[number]
            answer += 'L'
        elif number in [3, 6, 9]:
            r = dic[number]
            answer += 'R'
        else:
            x, y = dic[number]
            l_d = abs(x - l[0]) + abs(y - l[1])
            r_d = abs(x - r[0]) + abs(y - r[1])
            print(l_d, r_d)
            if l_d < r_d or (l_d == r_d and hand == 'left'):
                l = dic[number]
                answer += 'L'
            elif r_d < l_d or (r_d == l_d and hand == 'right'):
                r = dic[number]
                answer += 'R'

    return answer