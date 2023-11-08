def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n):
        cnt_data = prices[i]
        count=0
        for j in range(i+1,n):
            next_data = prices[j]
            count+=1
            if cnt_data > next_data:
                break

        answer.append(count)
    return answer

def solution2(prices):
	stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
		while stack and stack[-1][1] > prices[i]:
			past, _ = stack.pop()
			answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer

