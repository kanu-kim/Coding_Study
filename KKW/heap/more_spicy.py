from heapq import heappush, heappop
def solution(scoville, K):
    answer = 0
    heap = scoville
    heap.sort()
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        
        first = heappop(heap)
        second = heappop(heap)
        
        heappush(heap,first+2*second)
        answer+=1
    return answer
