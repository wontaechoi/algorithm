def preprocess(info):
    info = info.replace('C#', 'H')
    info = info.replace('D#', 'I')
    info = info.replace('F#', 'J')
    info = info.replace('G#', 'K')
    info = info.replace('A#', 'L')
    return info


def solution(m, musicinfos):
    musics = []
    m_p = preprocess(m)
    for i, info in enumerate(musicinfos):
        start, end, name, melody = info.split(",")
        start_h, start_m = start.split(":")
        end_h, end_m = end.split(":")
        start_time = int(start_h) * 60 + int(start_m)
        end_time = int(end_h) * 60 + int(end_m)
        take_time = end_time - start_time
        melody_m = preprocess(melody)
        index = 0
        played = ''
        while len(played) < take_time:
            if index == len(melody_m):
                index = 0
            played += melody_m[index]
            index += 1

        musics.append((take_time, name, i, played))
    possible = []
    for music in musics:
        t, n, i, played = music
        if len(m_p) > len(played):
            continue
        if m_p in played:
            possible.append((t, n, i))
    possible.sort(key=lambda x: [-x[0], x[2]])
    answer = possible[0][1] if possible else '(None)'
    return answer