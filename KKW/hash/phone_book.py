# 1. sort 풀이 (속도 최저 114.81ms, 30.6MB)
def solution(phone_book):
    answer = True
    phone_book.sort()
    n = len(phone_book)
    for i in range(0,n-1):
            if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
                return False
    return True

# 2. hash 풀이 (속도 최저 440.42ms, 46.7MB)
def solution(phone_book):
    n = len(phone_book)
    # phone_book.sort(key=len) sort하면 약간 빨라짐 의미x
    hash_map = dict.fromkeys(phone_book)
    for i in range(0,n):
        temp=''
        for alphabet in phone_book[i][:-1]:
            temp += alphabet
            #print(temp,hash_map)
            if temp in hash_map:
                return False
    return True
