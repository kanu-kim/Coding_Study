def check(a,b,c):
    if a>b and a>c:
        return [1]
    elif b>a and b>c:
        return [2]
    elif c>a and c>b:
        return [3]
    elif a==b and a>c:
        return [1,2]
    elif a==c and a>b:
        return [1,3]
    elif b==c and c>a:
        return [2,3]
    else:
        return [1,2,3]
        
def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    sol = [0,0,0]
    for idx,data in enumerate(answers):
        if data == s1[idx%len(s1)]:
            sol[0]+=1
        if data == s2[idx%len(s2)]:
            sol[1]+=1
        if data == s3[idx%len(s3)]:
            sol[2]+=1
    for i,s in enumerate(sol):
        if s == max(sol):
            answer.append(i+1)
    #answer = check(c1,c2,c3)
    return answer
