def solution(sizes):
    row,col = 0,0
    for x,y in sizes:
        if x<y:
            x,y = y,x
        if x > row:
            row = x
        if y > col:
            col = y
    answer = row * col    
    return answer
