def preprocess(log):
    date, time, taken = log.split()
    h, m, s = map(float, time.split(":"))
    end_time = int((h * 60 * 60 + m * 60 + s) * 1000)
    taken = int(float(taken[:-1]) * 1000)
    return (end_time - taken + 1, end_time)


def solution(lines):
    line_list = []
    for line in lines:
        line_list.append(preprocess(line))
    answer = -1
    for i in range(len(line_list) - 1):
        s1, e1 = line_list[i]
        count = 1
        for j in range(i + 1, len(line_list)):
            s2, e2 = line_list[j]
            if e2 < s1:
                break
            if s2 < e1 + 1000:
                count += 1
        answer = max(answer, count)
    return answer if answer != -1 else 1