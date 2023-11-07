from collections import deque

def solution(priorities, location):
    que =deque(priorities)
    answer = 0

    while True:
        check = que.popleft()
        location-=1
        if len(que)>0 and check < max(que):
            que.append(check)
            if location == -1:
                location = len(que)-1
        else:
            answer+=1
            if location == -1:
                break
            
    return answer
