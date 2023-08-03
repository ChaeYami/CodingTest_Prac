# https://school.programmers.co.kr/learn/courses/30/lessons/140108

'''
cnt1 첫문자 개수, cnt2는 그 후 문자 개수
1. 처음 'a'가 나왔을 때 k라는 변수에 'a'를 저장하고 cnt1에 1을 추가
2. 그 후 'a'가 또 나왔으면 cnt1는 1이 더 추가돼서 2가 된다.
3. 'a'가 연속으로 3번 나왔기에 cnt1은 3이 된다.
4. 'b'가 나왔을 때 cnt2에 1을 더 해준다.
(cnt1=4, cnt2=2) ===> ["aaabba"]
5. ["aaabbacc"]가 될 땐 cnt1과 cnt2가 같아지는 순간이기 때문에 answer에 1을 더해준다.
6. 끝까지 반복

'''

def solution(s):
   answer = 0
   cnt1=0; cnt2=0
   for i in s:
       if cnt1==cnt2:
           answer+=1
           k=i
       if k==i:
           cnt1+=1
       else:
           cnt2+=1
       
   return answer


s1 = "banana"	# 3
s2 = "abracadabra"	# 6
s3 = "aaabbaccccabba"	# 3




# https://school.programmers.co.kr/learn/courses/30/lessons/138477

'''
1. 명예의 전당 리스트 생성 top_list
2. score 리스트에서 명예의전당 리스트에 하나씩 넣고
3. 명예의전당 리스트 길이가 k보다 커지면 if len(top_list)>k
4. 가장 작은 값 삭제 top_list.remove(min(top_list))
5. 현재 명예의전당 리스트의 최솟값을 answer 에 append
'''

def solution(k, score):
    answer = []
    top_list = []
    for i in score:
        top_list.append(i)
        if len(top_list)>k:
            top_list.remove(min(top_list))
        answer.append(min(top_list))
    return answer

k1 = 3
score1 = [10, 100, 20, 150, 1, 100, 200]	
# result = [10, 10, 10, 20, 20, 100, 100]

k2 = 4
score2 = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
# result = [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]

solution(k1, score1)
solution(k2, score2)



# https://school.programmers.co.kr/learn/courses/30/lessons/236798


'''
1-1. 약수의 개수 리스트 생성 num_divisor
1-2. i=1 부터 while문으로 i가 number+1 보다 작을 때 까지 반복

2. 약수 구하기
2-1.divisor_list 생성
2-2.for문으로 약수 구하기
2-3.divisor를 약수 리스트에 append
3. 갯수 구하기 - len(divisor_list)
4. num_divisor 리스트에서 limit보다 큰 원소를 power 로 바꿔주기
5. 다 더하기
'''

'''
# 1차 시도
def solution(number, limit, power):
    answer = 0
    num_divisor = []
    i = 1
    while i < number+1:
        divisor_lst=[]
        for divisor in range(1, i+1):
            if i % divisor == 0:
                divisor_lst.append(divisor)
        num_divisor.append(len(divisor_lst))
        i+=1
    for n in range(len(num_divisor)):
        if num_divisor[n] > limit:
            num_divisor[n] = power

    answer = sum(num_divisor)
    return answer

시간 복잡도는 O(number^2)
이는 number가 커질수록 실행 시간이 기하급수적으로 증가하게 됨

1. 불필요한 계산 줄이기:
현재 코드에서는 모든 i에 대해 1부터 i까지의 약수를 구하고 그 개수를 num_divisor 리스트에 저장한 뒤, limit보다 큰 개수를 power로 변경하고 모든 값을 더하는 방식으로 문제를 해결하고 있습니다. 하지만 이러한 방식은 매우 비효율적입니다.

2. 미리 계산한 결과 재활용하기:
약수의 개수를 빠르게 계산하는 방법을 사용하면 시간을 줄일 수 있습니다. 예를 들면, 10의 약수는 1, 2, 5, 10으로 총 4개입니다. 여기서 주목할 점은 10의 약수는 2와 5의 곱으로 이루어져 있습니다. 이러한 특성을 활용하여 약수의 개수를 빠르게 계산할 수 있습니다.
'''

# 코드개선, 2차시도

def solution(number, limit, power):
    answer = 0
    num_divisor = [0] * (number + 1)  # 약수 개수를 저장할 리스트 초기화

    for divisor in range(1, number + 1):
        for i in range(divisor, number + 1, divisor):
            num_divisor[i] += 1

    for n in range(1, number + 1):
        if num_divisor[n] > limit:
            num_divisor[n] = power

    answer = sum(num_divisor)
    return answer


number1 = 5
limit1 = 3
power1 = 2
# result1 = 10

number2 = 10
limit2 = 3
power2 = 2
# result2 = 21

solution(number1,limit1,power1)
solution(number2,limit2,power2)


'''
# 인상깊은 풀이
def cf(n): # 공약수 출력
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))
def solution(number, limit, power):
    return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])
'''