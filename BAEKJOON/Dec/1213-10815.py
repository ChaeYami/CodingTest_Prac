import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M =  int(sys.stdin.readline())
check_cards = list(map(int, sys.stdin.readline().split()))

dic = {}

for i in range(len(cards)):
    dic[cards[i]] = i
    
    
for m in range(M):
    if check_cards[m] in dic:
        print(1, end=' ')
        
    else:
        print(0, end=' ')