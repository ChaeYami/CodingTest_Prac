#  https://www.acmicpc.net/problem/12789

import sys
input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))
stack = []
now_turn = 1
for student in students:
    stack.append(student)
    while stack and stack[-1] == now_turn:
        stack.pop()
        now_turn +=1
    
if stack:
    print('Sad')
else:
    print('Nice')    
'''


def test(students, N):
    students = list(map(int, students.split()))

    stack = []
    now_turn = 1
    for student in students:
        stack.append(student)
        print(stack)
        while stack and stack[-1] == now_turn:
            stack.pop()
            now_turn +=1
            print(stack, now_turn)
     
    if stack:
        print('sad')
    else:
        print('nice')    
    
            
                
                
test('5 4 1 3 2',5)
test('5 2 1 4 3',5)
test('2 5 1 3 4',5)
test('2 1 5 3 4',5)

'''