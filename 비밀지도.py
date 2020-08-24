def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(arr1[i] | arr2[i])

    ans = []
    for i in range(n):
        temp = bin(answer[i])[2:]
        if len(temp) < n:
            while len(temp) < n:
                temp = '0' + temp
        t = ''
        for i in temp:
            if i == '1':
                t += '#'
            else:
                t += ' '
        ans.append(t)
    return ans