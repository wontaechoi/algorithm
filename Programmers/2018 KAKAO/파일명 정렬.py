def divide(file):
    index = 0
    head = ''
    while True:

        if file[index].isnumeric():
            head_index = index
            break
        if file[index].isalpha():
            head += file[index].lower()
        else:
            head += file[index]
        index += 1
    while True:
        if index >= len(file):
            number = int(file[head_index:])
            tail = ''
            break
        if not file[index].isnumeric():
            number = int(file[head_index:index])
            tail = file[index:]
            break
        index += 1
    return head, number, tail


def solution(files):
    ans = []
    for i, file in enumerate(files):
        head, number, tail = divide(file)
        ans.append((head, number, i))
    ans.sort(key=lambda x: [x[0], x[1], x[2]])
    answer = []
    for h, n, i in ans:
        answer.append(files[i])
    return answer