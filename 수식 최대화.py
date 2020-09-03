from itertools import permutations
import re
def calculate (n1,n2, o):
    if o =='+':
        return n1+n2
    elif o =='-':
        return n1-n2
    else:
        return n1*n2
def solution(expression):
    orders = list(permutations(['*', '-', '+']))
    numbers = []
    operands = []
    prev = expression[0]
    answer = 0
    for i in range(1, len(expression)):
        if expression[i].isnumeric():
            prev += expression[i]
        else:
            numbers.append(int(prev))
            operands.append(expression[i])
            prev=''
    numbers.append(int(prev))
    for order in orders:
        print(order)
        new_numbers = [i for i in numbers]
        new_operands = [i for i in operands]

        for o in list(order):
            new_op = []
            new_n = []
            if o not in new_operands:
                continue
            for i, op in enumerate(new_operands):
                if o == op:
                    n = calculate(new_numbers[i], new_numbers[i+1], op)
                    new_numbers[i+1] = n
                else:
                    new_n.append(new_numbers[i])
                    new_op.append(op)
            new_n.append(new_numbers[i+1])
            new_numbers = new_n
            new_operands = new_op
        answer = max(abs(new_numbers[0]), answer)
    return answer