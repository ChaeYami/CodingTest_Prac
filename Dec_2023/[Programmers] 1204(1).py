'''
올바른 괄호
https://school.programmers.co.kr/learn/courses/30/lessons/12909
'''

def solution(s):
    answer = True
    stack = []
    for char in s:
        if char in "(":
            stack.append(char)
            print(stack)
        else:
            if not stack:
                return False
            
            top = stack.pop()
            if top != ")":
                return False
    
    return True

print(solution("()()"))

