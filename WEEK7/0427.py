# 최댓값 만들기 (1)
#정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 
# return하도록 solution 함수를 완성해주세요.

# 풀이 1 : max 함수, remove 함수 사용하기! 
def solution(numbers):
    answer = 0
    # 가장 큰 값을 찾고
    # 두번째로 큰 값을 찾는다
    # numbers -> list
    max_num = max(numbers) # max 라는 배열에서 가장 큰 값을 return 
    
    # 배열에서 요소 삭제
    # del -> x번째 요소 삭제
    # pop(x) -> x번째 요소 끄집어내기
    # remove(x) -> 배열에서 가장 첫번째로 나오는 x값 삭제
    numbers.remove(max_num)
    max2_num = max(numbers)
    
    answer = max_num * max2_num
    
    return answer


# 풀이 2 : sort 사용하기!
def solution(numbers):
    answer = 0
    
    numbers.sort(reverse = True)
    answer = numbers[0] * numbers [1]
    return answer



print(solution([1,2,3,4,5])) # 20
print(solution([0,31,24,10,1,9])) # 744