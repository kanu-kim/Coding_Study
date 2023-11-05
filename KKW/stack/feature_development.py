def solution(progresses, speeds):
    work_day=[]
    for p,s in zip(progresses,speeds):
        if len(work_day)==0 or work_day[-1][0] < -((p-100)//s):
            work_day.append([-((p-100)//s),1])
        else:
            work_day[-1][1]+=1
    answer = [i[1] for i in work_day]
    return answer
