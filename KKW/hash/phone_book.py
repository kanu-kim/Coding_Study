def solution(phone_book):
    answer = True
    phone_book.sort()
    n = len(phone_book)
    for i in range(0,n-1):
            if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
                return False
    return True
