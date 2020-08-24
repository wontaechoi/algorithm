def solution(dartResult):
    score = []
    check_ten = False
    for dart in dartResult:
        if dart.isnumeric():
            if not check_ten:
                score.append(int(dart))
                check_ten = True
            else:
                score[-1] = 10
                check_ten = False
        elif dart.isalpha():
            check_ten = False
            if dart == 'S':
                score[-1] = score[-1] **1
            elif dart == 'D':
                score[-1] = score[-1] **2
            elif dart =='T':
                score[-1] = score[-1] **3
        else:
            check_ten = False
            if dart == '*':
                if len(score) == 1:
                    score[-1] = score[-1] * 2
                else:
                    score[-1] = score[-1] * 2
                    score[-2] = score[-2] * 2
            elif dart == '#':
                score[-1] = -score[-1]
    return sum(score)