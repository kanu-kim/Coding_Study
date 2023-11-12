def prime(n):
    prime_set = [False,False]+[True]*n
    end = int(n**(0.5))+1
    for i in range(2,end):
        if prime_set[i] == True:
            for j in range(i+i,n,i):
                prime_set[j]= False
    
    return [i for i in range(n) if prime_set[i]==True]

def permutation(arr,r):
    n = len(arr)
    for i in range(n):
        if r == 1:
            yield [arr[i]]
        else:
            for next in permutation(arr[:i]+arr[i+1:],r-1):
                yield [arr[i]]+next

def solution(numbers):
    answer = 0
    # h : 만들 수 있는 가장 큰수
    g = list(map(lambda x:int(x),numbers))
    g.sort(reverse=True)
    g = list(map(lambda x:str(x),g))
    h = int(''.join(g))
    
    # num_list : 조각 수들의 리스트, prime_number : 2부터 h까지 소수의 집합
    num_list = list(numbers)
    prime_number = prime(h+1)
    
    # set_list : 조각 수로 만들 수 있는 순열 리스트
    set_list = []
    for i in range(1,len(num_list)+1):
        x = permutation(num_list,i)
        for j in x:
            set_list.append(int(''.join(j)))
    set_list = list(set(set_list))
    
    # 조각 수로 만든 값이 소수면 answer+=1
    for i in set_list:
        if i in prime_number:
            answer+=1
    return answer
