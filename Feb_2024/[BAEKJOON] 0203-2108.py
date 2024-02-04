import sys

input = sys.stdin.readline

n = int(input()) # 숫자 갯수
given_nums = [int(input()) for _ in range(n)] # 주어진 수

'''산술평균 구하기'''
total_sum = sum(given_nums) # 주어진 수들의 총합
a_mean = round(total_sum/n)

'''중앙값 구하기'''
given_nums.sort()
median = given_nums[n//2]

'''최빈값 구하기'''
num_count = dict() # 각 숫자의 갯수 - 숫자가 키, 갯수가 값
for num in given_nums:
        num_count[num] = num_count.get(num, 0) + 1
        
# 갯수가 가장 많을 때 그 갯수
max_count = max(num_count.values()) 

# 최빈값 리스트 (여러개일 경우도 있음)
mode_numbers = [key for key, value in num_count.items() if value == max_count]

# 최빈값, 하나라면 그 수를 출력하고, 여러개라면 최빈값 중 두 번째로 작은 값 출력
mode = mode_numbers[0] if len(mode_numbers) == 1 else sorted(mode_numbers)[1]
    
'''범위 구하기'''
num_range = given_nums[-1] - given_nums[0]

'''출력'''

print(a_mean)
print(median)
print(mode)
print(num_range)