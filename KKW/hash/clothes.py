def solution(clothes):
    answer = 1
    dic={}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]]+=1
        else:
            dic[i[1]]=1
    c_list = []

    # 최적화 가능한 영역 - dic values() 를 따로 저장하지 않고
    for i in dic:
        c_list.append(dic[i])

   #for i in dic.values(): 사용
    for i in c_list:
        answer*=(i+1)
    answer -= 1
    return answer
