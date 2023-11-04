# my solution

def solution(genres, plays):
    answer = []
    dic={}
    sort_dic={}
    for i in range(len(genres)):
        if genres[i] in dic:
            if plays[dic[genres[i]][0]] < plays[i]:
                dic[genres[i]] = [i,dic[genres[i]][0]]
            elif len(dic[genres[i]]) == 1 and plays[dic[genres[i]][0]] >= plays[i]:
                dic[genres[i]] = [dic[genres[i]][0],i]
            elif len(dic[genres[i]]) == 2 and plays[dic[genres[i]][1]] < plays[i] or plays[dic[genres[i]][0]] == plays[i]:
                dic[genres[i]] = [dic[genres[i]][0],i]
        else:
            dic[genres[i]] = [i]

        if genres[i] in sort_dic:
            sort_dic[genres[i]] += plays[i]
        else:
            sort_dic[genres[i]] = plays[i]

    sort_genres = sorted(sort_dic,key=lambda x:sort_dic[x],reverse=True)
    
    for i in sort_genres:
        answer.extend(dic[i])

    
    return answer

# simple solution
def solution(genres, plays):
    answer = []
    dic={}
    sum_dic={}
    for i,(g,p) in enumerate(zip(genres,plays)):
        if g in dic:
            dic[g].append((i,p))
        else:
            dic[g] = [(i,p)]
    
        if g in sum_dic:
            sum_dic[g] += p
        else:
            sum_dic[g] = p

    
    print(dic)
    
    for g,total in sorted(sum_dic.items(),key=lambda x:x[1],reverse=True):
        for idx,p in sorted(dic[g],key = lambda x :x[1],reverse=True)[:2]:
            answer.append(idx)
    return answer
