import heapq
def solution(jobs):
    answer = 0
    jobs.sort()
    # 중요한 키 : que가 비어있을때, 요청이 있는 것 부터 시작 que가 비어있지 않다면 소요시간이 짧은 순
    n = len(jobs)
    disk = 0
    idx = 0
    end = 0
    que=[]
    time=0
	# 개선점 : time++ // jobs들 사이 공백시간을 단축시키는 방법 찾기
    while disk or idx<n:
        if disk and time == end:
            disk = 0
        while idx<n and time == jobs[idx][0]:
            heapq.heappush(que,[jobs[idx][1],jobs[idx][0]])
            idx+=1
        if not disk and que:
            x = heapq.heappop(que)
            end = time + x[0]
            answer += (end - x[1])
            disk=1
        time+=1
    return answer//n
