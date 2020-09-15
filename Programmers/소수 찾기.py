from itertools import permutations


def isPrime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    number = []
    for c in numbers:
        number.append(c)
    count = 0
    checked = []
    for i in range(1, len(numbers) + 1):
        x = list(permutations(number, i))
        for c in x:
            temp = ''
            for n in c:
                temp += n
            checked.append(int(temp))
    for temp in set(checked):
        if isPrime(int(temp)):
            count += 1
    return count