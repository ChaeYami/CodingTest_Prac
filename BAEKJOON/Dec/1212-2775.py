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
    
    # 호수를 키, 사람 수를 값으로 하는 딕셔너리 생성
    floor={}
    
    # 0층 업데이트
    for i in range(1,n+1):
        floor[i] = i
     
    # ex) {1 : 1, 2 : 2, 3 : 3}   
        
    # 그 위의 층
    for i in range(k):    
        # 1호는 어차피 1명이므로 2호부터 시작, 1호부터 하면 j-1에서 에러 발생
        for j in range(2,n+1):
            floor[j] = floor[j-1] + floor[j]
            
    # ex) {1 : 1, 2 : 4, 3 : 10}

    print(floor[n])
        