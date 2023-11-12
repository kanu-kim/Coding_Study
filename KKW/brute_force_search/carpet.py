def solution(b, y):
    # y의 격자 크기 row, col
    # y = row*col
    # b = row*2 + col*2 + 4
    # 연립 후 근의 공식으로 col 구하기 
    ss = ((b/2-2)**2-(4*y))**0.5
    col = ((b/2-2)-ss)/2
    row = int(y/col)
    
    return [row+2,col+2]
