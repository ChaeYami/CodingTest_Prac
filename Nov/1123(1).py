def solution(s):
    answer = 0
    str_ = {'zero':'0', 'one':'1', 'two':'2', 'three' : '3' ,'four' : '4', 'five' :'5',  'six' : '6', 'seven' : '7' ,'eight' :'8',  'nine' :'9' }
    
    for i in str_.keys():
        if i in s:
            s = s.replace(i,str_[i])

    answer = int(s)
    return answer

print(solution("one4seveneight"))