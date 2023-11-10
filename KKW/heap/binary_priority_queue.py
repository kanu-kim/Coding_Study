import heapq
def solution(operations):
    heap=[]
    for i in operations:
        if i == "D -1" and heap:
            heapq.heappop(heap)
            #print("min pop")
        elif i == "D 1" and heap:
            heap.pop()
            #print("max pop")
        elif i[0] == "I":
            x = int(i.split(' ')[1])
            heapq.heappush(heap,x)
            #print("push")
    if heap:
        return [max(heap),min(heap)]
    return [0,0]
