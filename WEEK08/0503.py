# 로그인 성공?

'''
입력한 아이디와 패스워드가 담긴 배열 id_pw
회원들의 정보가 담긴 2차원 배열 db
로그인 성공, 실패에 따른 메시지를 return

아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return
로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”
아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return

제한사항

아이디는 문자열, 알파벳 소문자와 숫자로만
패스워드는 숫자로 구성된 문자열
회원들의 비밀번호는 같을 수 있지만 아이디는 같을 수 없습니다.
id_pw의 길이는 2
id_pw와 db의 원소는 [아이디, 패스워드] 형태
1 ≤ 아이디의 길이 ≤ 15
1 ≤ 비밀번호의 길이 ≤ 6
1 ≤ db의 길이 ≤ 10
db의 원소의 길이는 2
'''

def solution(id_pw, db):
    # db에서 해당 아이디랑 비밀번호가 있는지 확인을 하고
    for account in db:
    # if/elif/else 이용해서 조건에 맞으면 값을 리턴
        if id_pw[0] == account[0]:
            if id_pw[1] == account[1]:
                return "login"
            else:
                return "wrong pw"
    
    return "fail"

print(solution(["meosseugi", "1234"],[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]])) # login
print(solution(["programmer01", "15789"],[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]])) # wrong pw
print(solution(["rabbit04", "98761"],[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]])) # fail