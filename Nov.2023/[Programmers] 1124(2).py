# https://school.programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
import re

def calculation_func(num1, num2, oper):
    if oper == "+":
        return str(int(num1) + int(num2))
    elif oper == "-":
        return str(int(num1) - int(num2))
    elif oper == "*":
        return str(int(num1) * int(num2))
    
def operation_func(exp_list, operations):
    for oper in operations:
        stack = []
        while len(exp_list) != 0:
            temp = exp_list.pop(0)
            if temp == oper:
                stack.append(calculation_func(stack.pop(),exp_list.pop(0),oper))
                print(stack)
            else:
                stack.append(temp)
        exp_list = stack
        
    # return abs(int(exp_list[0]))
                

def solution(expression):
    answer = 0
    operator = ['+', '-', '*']
    operation_case = list(permutations(operator, 3)) # 우선순위
    
    exp_list = re.split('(\D)', expression)
    
    print(exp_list)
    print(operation_case)
    
    answer_lst = []
    for operations in operation_case:
        answer_lst.append(operation_func(exp_list, operations))
        
    print(answer_lst)


    
    return answer





print(solution("100-200*300-500+20"	))