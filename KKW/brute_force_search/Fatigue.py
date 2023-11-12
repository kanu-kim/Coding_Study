# my solution
def	tour(z,k,dungeons):
    n_max=0
    depth=z
    for i in dungeons:
        n=0
        hp=k
        if(i[0]<=k):
            n+=1
            hp-=i[1]
            new = [x for x in dungeons if i!=x]
            n+=tour(depth+1,hp,new)
        if(n>n_max):
            n_max = n
    return n_max

def solution(k, dungeons):
    answer = -1
    answer = tour(0,k,dungeons)
    return answer

# other solution1

answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0

def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer

# other solution2

def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key = lambda x : ((x[1]+x[0])/x[0],x[1]))
    for x,y in dungeons:
        print("x :", x, "y : ", y)
        if k >= x:
            k -= y
            answer += 1
    return answer
