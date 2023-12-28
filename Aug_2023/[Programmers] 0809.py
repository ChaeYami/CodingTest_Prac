# https://school.programmers.co.kr/learn/courses/30/lessons/133502

'''
햄버거 가게에서 일을 하는 상수는 햄버거를 포장하는 일을 합니다. 함께 일을 하는 다른 직원들이 햄버거에 들어갈 재료를 조리해 주면 조리된 순서대로 상수의 앞에 아래서부터 위로 쌓이게 되고, 상수는 순서에 맞게 쌓여서 완성된 햄버거를 따로 옮겨 포장을 하게 됩니다. 상수가 일하는 가게는 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 햄버거만 포장을 합니다. 상수는 손이 굉장히 빠르기 때문에 상수가 포장하는 동안 속 재료가 추가적으로 들어오는 일은 없으며, 재료의 높이는 무시하여 재료가 높이 쌓여서 일이 힘들어지는 경우는 없습니다.

예를 들어, 상수의 앞에 쌓이는 재료의 순서가 [야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]일 때, 상수는 여섯 번째 재료가 쌓였을 때, 세 번째 재료부터 여섯 번째 재료를 이용하여 햄버거를 포장하고, 아홉 번째 재료가 쌓였을 때, 두 번째 재료와 일곱 번째 재료부터 아홉 번째 재료를 이용하여 햄버거를 포장합니다. 즉, 2개의 햄버거를 포장하게 됩니다.

상수에게 전해지는 재료의 정보를 나타내는 정수 배열 ingredient가 주어졌을 때, 상수가 포장하는 햄버거의 개수를 return 하도록 solution 함수를 완성하시오.

* ingredient의 원소는 1, 2, 3 중 하나의 값이며, 순서대로 빵, 야채, 고기를 의미합니다.
'''

'''
빵 – 야채 – 고기 - 빵 : [1,2,3,1]
찾는 함수
def solution(ingredient):
    answer = 0
    for i in range(len(ingredient)-3):
        if ingredient[i:i+4] == [1, 2, 3, 1]:
            answer += 1
    return answer
'''

'''
# 햄버거를 만들고 남은 재료로 또 만들수 있는지 확인해야 하므로 for문을 다시 반복해야 함
def solution(ingredient):
    answer = 0
    while True:
        found_pattern = False
        for i in range(len(ingredient)-3):
            if ingredient[i:i+4] == [1, 2, 3, 1]:
                found_pattern = True
                answer += 1
                ingredient = ingredient[:i] + ingredient[i+4:]
                break  # 패턴을 찾았으면 더 이상 검사하지 않음
        if not found_pattern:
            break  # 더 이상 패턴을 찾지 못하면 종료
    return answer
    
#->시간초과
'''

def solution(ingredient):
    answer = 0
    stack = []  # 패턴을 검사할 때 사용할 스택

    for i in ingredient:
        stack.append(i)  # 현재 재료를 스택에 추가
        stack_len = len(stack)

        # 스택의 길이가 4 이상이면 패턴 검사
        if stack_len >= 4:
            # 스택의 마지막 4개 요소가 [1, 2, 3, 1]인지 확인
            if stack[-4:] == [1, 2, 3, 1]:
                # 패턴을 찾았으므로 스택에서 제거하고 answer 증가
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1

    return answer


ingredient1 = [2, 1, 1, 2, 3, 1, 2, 3, 1]
ingredient2 = [1, 3, 2, 1, 2, 1, 3, 1, 2]	
print(solution(ingredient1)) # 2
print(solution(ingredient2)) # 0