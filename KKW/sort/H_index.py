def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i>=citations[i]:
            break
        answer += 1
    return answer

# test code
# input:[3,0,6,1,5] 
# return 3

print(solution([3,0,6,1,5]))
