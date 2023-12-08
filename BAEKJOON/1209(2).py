# https://wookcode.tistory.com/49

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    brackets = input()
    stack = []
    result=""
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)  
        elif bracket == ')':
            if stack:
                stack.pop()
                
            else:
                result="NO"
    if not stack and result!= "NO":
        result="YES"
        
    else:
        result="NO"
        
    
    print(result)

''''''
# def test(brackets):
#     stack = []
#     result=""
#     # brackets = input()
#     for bracket in brackets:
#         if bracket == '(':
#             stack.append(bracket)  
#         else:
#             if not stack:
#                 result="NO"
#             else:
#                 stack.pop()
#     if stack:
#         result="NO"
#     elif not stack and result != "NO":
#         result="YES"

#     print(result)
    
# test("(())())")
# test("(((()())()")
# test("(()())((()))")
# test("((()()(()))(((())))()")
# test("()()()()(()()())()")
# test("(()((())()(")

# test("((")
# test("))")
# test("())(()")