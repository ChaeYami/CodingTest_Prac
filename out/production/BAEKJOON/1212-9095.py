# https://www.acmicpc.net/problem/9095

T = int(input())


for _ in range(T):
    def Recur(num):
        if num == 1:
            return 1
        elif num ==2:
            return 2
        elif num ==3:
            return 4
        else:
            return (Recur(num-3)+Recur(num-2)+Recur(num-1))
    n = int(input())
    print(Recur(n))