import re


def solution(word, pages):
    answer = 0
    link_dict = {}
    ext = []
    score = []
    link_score = []
    for n, page in enumerate(pages):
        p = page.split('<')
        links = []
        count = 0
        for i, s in enumerate(p):
            strip = s.strip()
            if strip.startswith('meta property="og:url"'):
                current = strip.split('"')[-2]
            if strip.startswith('a href='):
                links.append(strip.split('"')[1])
        link_dict[current] = n
        ext.append(links)
        for s in page.split('body>')[1].split("\n"):
            for ss in re.split(r'<a', s):
                for z in re.split(r'</a>', ss):
                    zz = re.sub(r'[^a-zA-Z]', ' ', z).split()
                    for zzz in zz:
                        if zzz.lower() == word.lower():
                            count += 1
        score.append(count)
        s = count / len(links) if links else 0
        link_score.append(s)
    all_score = [0 for _ in range(len(pages))]

    for i, ex in enumerate(ext):
        for link in ex:
            if link in link_dict:
                all_score[link_dict[link]] += link_score[i]
    answer = []
    for i in range(len(pages)):
        answer.append((i, all_score[i] + score[i]))
    answer.sort(key=lambda x: [-x[1], x[0]])
    return answer[0][0]