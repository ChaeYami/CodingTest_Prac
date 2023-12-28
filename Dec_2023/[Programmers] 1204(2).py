'''
전화번호 목록
'''
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    phone_dict = {}
    
    for phone_number in phone_book:
        phone_dict[phone_number] = 1
        
    for phone_number in phone_book:
        tem = ""
        for number in phone_number:
            tem += number
            if tem in phone_dict and tem != phone_number:
                answer = False
                
    return answer

def solution(phone_book):
    phone_book.sort() 

    for i in range(len(phone_book)):
        if i == len(phone_book)-1:
            break
        
        now_num = phone_book[i]
        compare_num = phone_book[i+1]
        
        if now_num in compare_num and compare_num.index(now_num) == 0:
            return False

    return True

