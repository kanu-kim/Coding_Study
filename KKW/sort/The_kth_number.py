def solution(array, commands):
    answer = []
    for i,j,k in commands:
    	answer.append(sorted(array[i-1:j])[k-1])
    return answer

# test case
# [1,2,3,4,5], [1,2,3] 2nd is [2]
print(solution([1,2,3,4,5],[[1,3,2]]))
