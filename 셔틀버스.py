def change_timetable(timetable):
    new_timetable = []
    for tt in timetable:
        h, m = tt.split(':')
        new_timetable.append(int(h) * 60 + int(m))
    new_timetable.sort()
    return new_timetable


def get_bus_schedule(n, t):
    start_hour = 540
    schedule = []
    for i in range(n):
        schedule.append(540 + i * t)
    return schedule, [0 for _ in range(len(schedule))]


def convert_time(time):
    hour, minute = time // 60, time % 60
    return "{0:02}:{1:02}".format(hour, minute)


def solution(n, t, m, timetable):
    schedule, capacity = get_bus_schedule(n, t)
    timetable = change_timetable(timetable)
    index = 0
    last_time = 0
    for n, s in enumerate(schedule):
        while index < len(timetable):
            time = timetable[index]
            if time <= s and capacity[n] < m:
                capacity[n] += 1
                index += 1
                last_time = time
            else:
                break
    last = False if capacity[-1] < m else True
    answer = 540
    if not last:
        answer = schedule[-1]
    else:
        index = index if index < len(timetable) else index - 1
        answer = last_time - 1
    answer = convert_time(answer)
    return answer