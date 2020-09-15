import re
from itertools import permutations
def solution(user_id, banned_id):
    N = len(banned_id)
    possible = list(permutations(user_id,len(banned_id)))
    can = []
    for pos in possible:
        temp = []
        flag = False
        for x in range(len(pos)):
            if not re.match( banned_id[x].replace('*','.'), pos[x]) or len(pos[x]) != len(banned_id[x]):
                break
            temp.append(pos[x])
        temp.sort()
        if len(temp) ==N and temp not in can:
            can.append(temp)
    return len(can)