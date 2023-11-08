from collections import deque

def solution(priorities, location):
    que =deque(priorities)
    answer = 0

    while True:
        check = que.popleft()
        location-=1
        if que and check < max(que):
            que.append(check)
            if location == -1:
                location = len(que)-1
        else:
            answer+=1
            if location == -1:
                break
            
    return answer

def solution2(priorities, location):
    que = [(data,i) for i,data in enumerate(priorities)]
    answer = 0

    while True:
        cnt_data = que.pop(0)
        if que and cnt_data[0] < max(que)[0]:
            que.append(cnt_data)
        else:
            answer+=1
            if cnt_data[1] == location:
                return answer
