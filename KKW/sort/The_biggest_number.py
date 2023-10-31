def check(a,b):
    la,lb = len(a),len(b)
    x=0
    if la>lb:
        max_len = la
    else:
        max_len = lb
    while True:
        if a[x%la] > b[x%lb]:
            return 0
        elif a[x%la] < b[x%lb]:
            return 1
        if x > max_len:
            return 0
        x+=1

def solution(numbers):
    # string으로 변환 후 간단한 정렬
    array=sorted(list(map(lambda x:str(x),numbers)),reverse=True)
    #print(array)
    n = len(array)
    # 삽입정렬
    for i in range(1,n):
        key = array[i]
        for j in range(i,0,-1):
            # key가array의 앞 요소보다 크다면 1 아니면 0
            if check(array[j-1],key):
                array[j]=array[j-1]
                # for 문에서 j==1이면 end되므로 j=0대입
                j-=1
            else:
                break
        array[j] = key
    #print(array)
    answer = ''.join(array)
    # test case 11번: [0,0,0] -> "0", "000"으로 출력하지 않도록 조심
    if answer[0] == '0':
        return "0"
    else:
        return answer
