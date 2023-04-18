# ============================== 영어가 싫어요 ============================== 

def solution(numbers):
    answer = 0
    # 문자열을 단어로 분리
    # 각 단어를 인식해서 숫자로 변환한다.
    
    number_dict = {"zero" : 0, "one" : 1, "two":2, "three" : 3, "four":4, "five": 5, "six": 6, "seven" : 7, "eight" : 8, "nine": 9}
    
    # num_string = ""
    
    for key,value in number_dict.items():
        val = str(value)
        numbers = numbers.replace(key,val)
        #num = numbers.replace(key,val) 안됨 ! 다른 변수에 넣어버리면 for문을 돌면서 replace가 업데이트 되지 않는다. 계속 기존 numbers로 덮어씌워짐
        # numbers.replace(key,val) --> replace는 변수에 넣어줘야 한다
    return int(numbers)


numbers1 = 'onetwothreefourfivesixseveneightnine'
numbers2 = 'onefourzerosixseven'

print(type(solution(numbers1)))
print(solution(numbers2))

# 123456789
# 14067

def solution(numbers):
    dic = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
        "zero" : 0
    }
    answer = 0
    i = 0
    j = 1
    N = len(numbers)
    while i<N:
        var = dic.get(numbers[i:j],False)
        if type(var) == int:
            answer *= 10
            answer += var
            i = j
            j += 1
        else:
            j += 1
    return answer

# ============================== 가위바위보 ============================== 

def solution(rsp): # 205 
    rsp_dict = {
        '0':'5',
        '5':'2',
        '2': '0'
    }
    rsp_str = ''
    
    for i in rsp:
        rsp_str += rsp_dict[i] 
        
    return rsp_str
        
    


print(solution('205'))