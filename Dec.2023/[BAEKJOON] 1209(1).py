import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    command = int(input())
    
    if command != 0:
        stack.append(command)
        
    else:
        stack.pop()
        
if stack:
    sum_stack = sum(stack)
else:
    sum_stack = 0
        
print(sum_stack)