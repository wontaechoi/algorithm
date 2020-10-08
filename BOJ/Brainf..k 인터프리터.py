N = int(input())
for n in range(N):
    sm, sc, si = map(int, input().split())
    memory = [0 for i in range(sm)]
    index = 0
    char_index = 0
    command = str(input())
    input_char = str(input())

    loop_dic = {}
    loop_stack = []
    for i in range(sc):
        if command[i] == '[':
            loop_stack.append(i)
        elif command[i] == ']':
            ind = loop_stack.pop()
            loop_dic[i] = ind
            loop_dic[ind] = i
    i = 0
    count = 0
    max_index = 0
    while i < sc:
        c = command[i]
        if c == '-':
            memory[index] = memory[index] - 1 if memory[index] != 0 else 255

        elif c == '+':
            memory[index] = memory[index] + 1 if memory[index] != 255 else 0

        elif c == '<':
            index = index - 1 if index != 0 else sm - 1

        elif c == '>':
            index = index + 1 if index != sm - 1 else 0

        elif c == ',':
            if char_index < si:
                memory[index] = ord(input_char[char_index])
                char_index += 1
            else:
                memory[index] = 255

        elif c == '[':
            if memory[index] == 0:
                i = loop_dic[i] - 1
        elif c == ']':
            if memory[index] != 0:
                i = loop_dic[i] - 1
        i += 1
        max_index = max(i, max_index)
        count += 1
        if count >= 50000000:
            break
    if i == sc:
        print('Terminates')
    else:
        print('Loops {} {}'.format( loop_dic[max_index], max_index))
