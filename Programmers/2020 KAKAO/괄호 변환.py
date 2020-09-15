def divide_balanced(s):
    count1 = 0
    count2 = 0
    for n, i in enumerate(s):
        if i == '(':
            count1 += 1
        elif i == ')':
            count2 += 1
        if count1 == count2:
            if n + 1 != len(s):
                return s[:n + 1], s[n + 1:]
            else:
                return s, ''


def sol(p):
    if p == '':
        return p
    if check_correct(p):
        return p
    u, v = divide_balanced(p)
    if check_correct(u):
        return u + sol(v)
    else:
        t = '(' + sol(v) + ')'
        new_u = reverse_string(u[1:-1])
        return t + new_u


def reverse_string(s):
    new_s = ''
    for i in range(len(s)):
        if s[i] == '(':
            new_s += ')'
        else:
            new_s += '('
    return new_s


def check_correct(s):
    count1 = 0
    count2 = 0
    for c in s:
        if c == '(':
            count1 += 1
        elif c == ')':
            count2 += 1
        if count2 > count1:
            return False
    return True


def solution(p):
    answer = sol(p)
    return answer