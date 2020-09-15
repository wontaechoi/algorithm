import re


def clear(words):
    return re.sub(r'[^a-zA-Z]', "", words).lower()


def bigram(words):
    bigram = []
    dic = {}
    for i in range(len(words) - 1):
        word = words[i:i + 2].lower()
        flag = True
        for c in word:
            if not c.isalpha():
                flag = False
                break
        if flag:
            bigram.append(word)
            if word not in dic:
                dic[word] = 0
            dic[word] += 1

    return set(bigram), dic


def solution(str1, str2):
    bigram1, dic1 = bigram((str1))
    bigram2, dic2 = bigram((str2))
    intersect = list(bigram1.intersection(bigram2))
    uni = list(bigram1.union(bigram2))
    numerator = 0
    for inter in intersect:
        numerator += min(dic1[inter], dic2[inter])
    denominator = 0
    for un in uni:
        if un in dic1 and un in dic2:
            denominator += max(dic1[un], dic2[un])
        elif un in dic1:
            denominator += dic1[un]
        else:
            denominator += dic2[un]

    answer = int(numerator / denominator * 65536) if denominator != 0 else 65536
    return answer