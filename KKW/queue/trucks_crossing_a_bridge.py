from collections import deque
def solution1(bridge_length, weight, truck_weights):
    n = len(truck_weights)
    que=deque()
    head = 0
    ht = 0
    time_list=[]
    
    time = 1
    while len(que)!=0 or head < n:
        #print("first",time,que,time_list)
        if head<n and sum(que) + truck_weights[head] <= weight:
            que.append(truck_weights[head])
            time_list.append(time-1)
            head+=1
            #print("1 que and head",que,head)
        if time - time_list[ht] == bridge_length:
            que.popleft()
            ht+=1
            #print("2 que",que)
        time += 1
    return time

# good other solution

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step

