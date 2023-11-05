# 294ns
def solution(arr):
    answer = []
    check = -1
    for i in arr:
        if i==check:
            continue
        else:
            answer.append(i)
            check = i
    return answer

# 355ns
def solution(arr):
    answer = [arr[0]]
    for i in arr[1:]:
        if answer[-1]!=i:
            answer.append(i)
    return answer
