
from collections import deque

import sys
input = sys.stdin.readline

N = int(input())

deq = deque()
for _ in range(N):
    input_lst = (input().replace('''\n''','')).split(' ')
    
    if input_lst[0] == 'push':
        deq.append(input_lst[1])
    elif input_lst[0] == 'pop' and deq:
        print(deq.popleft())
    elif input_lst[0] == 'pop'and not deq:
        print('-1')
    elif input_lst[0] == 'size':
        print(len(deq))
    elif input_lst[0] == 'empty' and deq:
        print('0')
    elif input_lst[0] == 'empty' and not deq:
        print('1')
    elif input_lst[0] == 'front' and deq:
        print(deq[0])
    elif input_lst[0] == 'front' and not deq:
        print('-1')
    elif input_lst[0] == 'back' and deq:
        print(deq[-1])
    elif input_lst[0] == 'back' and not deq:
        print('-1')
        
    
        
    
# test('push 1')
# test('push 2')
# test('front')
# test('back')
# test('size')
# test('empty')
# test('pop')
# test('pop')
# test('pop')
# test('size')
# test('empty')
# test('pop')
# test('push 3')
# test('empty')
# test('front')