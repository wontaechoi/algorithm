import sys

sys.setrecursionlimit(10 ** 7)


def sol(room, dic):
    if room not in dic:
        dic[room] = room + 1
        return room

    r = sol(dic[room], dic)
    dic[room] = r
    return r


def solution(k, room_number):
    dic = {}
    answer = []
    for room in room_number:
        room = sol(room, dic)
        answer.append(room)
    return answer