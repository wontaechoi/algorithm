#https://programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    answer = []
    genre_dict = {}
    i = 0
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in genre_dict:
            genre_dict[g] = (p, [(i,p)])
        else:
            genre_dict[g] = (genre_dict[g][0]+p, genre_dict[g][1]+[(i,p)])
    print(list(genre_dict.values()))
    genre = sorted(list(genre_dict.values()), reverse= True)
    answer = []
    for x, y in genre:
        y.sort(key = lambda x: [-x[1], x[0]])
        for i in range(len(y)):
            if i >1:
                break
            answer.append(y[i][0])
    return answer