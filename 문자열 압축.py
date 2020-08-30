def solution(s):
    N = len(s)
    answer = N
    for n in range(1, N + 1):
        i = n
        count = 1
        prev = s[0:n]
        gram = ''
        while i < N:
            if i + n > N:
                cur = s[i:]
            else:
                cur = s[i: i + n]
            if prev != cur:
                if count > 1:
                    gram += '{}{}'.format(count, prev)
                else:
                    gram += prev
                prev = cur
                count = 1
            else:
                count += 1

            i += n
        if count > 1:
            gram += '{}{}'.format(count, prev)
        else:
            gram += prev
        answer = min(answer, len(gram))

    return answer