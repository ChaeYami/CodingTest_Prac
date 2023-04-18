# ============= 배열 두 배 만들기 ============= 

def solution(numbers):
    answer = []
    for i in numbers:
        j = i*2
        answer.append(j)
    return answer

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 100, -99, 1, 2, 3]

print(solution(numbers1))
print(solution(numbers2))

# 리스트 컴프리헨션 쓰는 방법!
def solution(numbers):
    return [num*2 for num in numbers]

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 100, -99, 1, 2, 3]

print(solution(numbers1))
print(solution(numbers2))


# ============= 배열 뒤집기 ============= 

def solution(num_list):
    num_list.reverse()
    return num_list

a = [1, 2, 3, 4, 5]
b = [1, 1, 1, 1, 1, 2]
c = [1, 0, 1, 1, 1, 3, 5]

print(solution(a))
print(solution(b))
print(solution(c))

# 슬라이싱 사용하기
def solution(num_list):
    return num_list[::-1] # num_list를 복사해서 return, 마지막거부터 출력한다.

def solution(num_list):
    answer = []
    for i in range(len(num_list)): # 배열 원소의 갯수만큼 반복
        j = num_list.pop() # 마지막 원소를 pop !
        answer.append(j)  # pop : 배열의 원소를 삭제하고, 삭제한 원소를 가져온다.
    return answer

a = [1, 2, 3, 4, 5]
b = [1, 1, 1, 1, 1, 2]
c = [1, 0, 1, 1, 1, 3, 5]

print(solution(a))
print(solution(b))
print(solution(c))


# ============= 문자열 뒤집기 ============= 

def solution(my_string):
    return my_string[::-1] 

a = "jaron"
b = "bread"

print(solution(a))
print(solution(b))
