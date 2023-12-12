# https://www.acmicpc.net/problem/2775

'''
a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
2층, 3호
1 | 2 | 3
1 | 1+2 | 1 + 2+3
1 | 1 + 1+2 | 1 + 1+2 + 1+2+3 
'''

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    
    zero_floor={}
    current_floor={}
    for i in range(1,n+1):
        zero_floor[i] = i

    for i in range(k):    
        for j in range(2,n+1):
            zero_floor[j] = zero_floor[j-1] + zero_floor[j]

    print(zero_floor[n])
        