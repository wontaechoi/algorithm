def convert(num, n):
    to_convert = '0123456789ABCDEF'
    if num < n:
        return to_convert[num]
    else:
        d, r = divmod(num, n)
        return convert(d, n) + to_convert[r]


def solution(n, t, m, p):
    to_say = ''
    num = 0
    while len(to_say) < t*m:
        for c in str(convert(num,n)):
            to_say += c
        num += 1
    answer = ''
    for i in range(len(to_say)):
        if i % m == (p-1):
            answer += to_say[i]
    return answer[:t]