def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = []
    b_weight = weight
    while truck_weights:
        new_bridge = []
        time += 1
        for n in range(len(bridge)):
            bridge[n] = (bridge[n][0] - 1, bridge[n][1])
            if bridge[n][0] > 0:
                new_bridge.append(bridge[n])
            else:
                b_weight += bridge[n][1]

        if truck_weights:
            if b_weight - truck_weights[0] >= 0:
                w = truck_weights.pop(0)
                b_weight -= w
                new_bridge.append((bridge_length, w))
        bridge = new_bridge

    time += bridge_length
    answer = time
    return answer