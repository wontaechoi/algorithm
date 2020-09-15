#https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    for i, num in enumerate(phone_book):
        for j in range(len(phone_book)):
            if i != j:
                if len(num) > len(phone_book[j]):
                    continue
                else:
                    if num == phone_book[j][:len(num)]:
                        return False
    return True