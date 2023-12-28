# https://school.programmers.co.kr/learn/courses/30/lessons/178870

'''
비내림차순으로 정렬된 수열이 주어질 때, 다음 조건을 만족하는 부분 수열을 찾으려고 합니다.

- 기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열이어야 합니다.
- 부분 수열의 합은 k입니다.
- 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾습니다.
- 길이가 짧은 수열이 여러 개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열을 찾습니다.

수열을 나타내는 정수 배열 sequence와 부분 수열의 합을 나타내는 정수 k가 매개변수로 주어질 때, 위 조건을 만족하는 부분 수열의 시작 인덱스와 마지막 인덱스를 배열에 담아 return 하는 solution 함수를 완성해주세요. 이때 수열의 인덱스는 0부터 시작합니다.
'''

'''
1. 특정 합을 가지는 부분 연속 수열 - 이건 그냥 투포인터
시작(start) 인덱스와 끝(end) 인덱스를 모두 0으로 시작해, 원하는 합이 나올 때 까지 end를 하나씩 증가시키고, 
start를 증가시키며 반복하는 방법
2. 또한 길이를 비교해줘야 하므로 각 start-end 를 비교해줘야 한다.
시작할 때 min_length를 지정하고 비교해서 업데이트 하는 방식
'''

def solution(sequence, k):
    answer = []
    min_length = float('inf')
    # 부분 수열 찾기 시작
    interval_sum = 0
    end = 0
    for start in range(len(sequence)):
        # end 증가
        while interval_sum < k and end < len(sequence):
            interval_sum +=sequence[end]
            end += 1
        # 합이 k 일때 
        if interval_sum == k:
            # 지금까지 중에 길이가 가장 짧을 경우
            if min_length > end-start:
                answer = [start, end-1]
            min_length = min(min_length, end-start)
            
        interval_sum -=sequence[start]
    return answer


sequence1 = [1, 2, 3, 4, 5]
k1 = 7
sequence2 = [1, 1, 1, 2, 3, 4, 5]
k2 = 5
sequence3 = [2, 2, 2, 2, 2]
k3 = 6

print(solution(sequence1, k1)) # [2,3]
print(solution(sequence2, k2)) # [6,6]
print(solution(sequence3, k3)) # [0,2]