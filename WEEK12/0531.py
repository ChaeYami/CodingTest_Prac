# https://school.programmers.co.kr/learn/courses/30/lessons/77484


"""
보이는 번호
가려진 번호

1. 보이는 번호로 일치하는 번호 갯수 확인 -> 그냥 전체에서 일치하는 갯수 구하면 되지 않을까?
2. 안 보이는 번호 갯수 세기
3. 안 보이는 번호가 모두 불일치일 때 - 최저순위
4. 안 보이는 번호가 모두 일치일 때 - 최고순위

일치하는 갯수
0개, 1개 - 6등
2개 - 5등
.
.
.
"""

# i = [1,1,3,4,5,3,3,7,6,8,9,3,2,5,9]

# print(i.count(3)) #리스트i에 요소3의 개수 구할때

# >>> 4


def solution_01(lottos, win_nums):
    zero_count = lottos.count(0)
    match_count = 0
    for num in lottos:
        if num in win_nums:
            match_count += 1  # 0포함 일치하는 숫자 갯수
    low_rank = min(7 - match_count, 6)  # 0이 다 틀렸다고 가정했을 때 등수 = 최저등수
    high_rank = min(7 - (match_count + zero_count), 6)  # 0이 다 맞았다고 가정했을 때 = 최고등수
    return [high_rank, low_rank]


print(solution_01([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3, 5]
print(solution_01([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1, 6]
print(solution_01([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1, 1]
print(solution_01([45, 4, 0, 0, 0, 0], [20, 9, 3, 45, 4, 35]))  # [1, 5]
print(solution_01([44, 1, 0, 0, 0, 25], [31, 10, 45, 2, 6, 19]))  # [4, 6]


def solution_02(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return [rank[cnt_0 + ans], rank[ans]]


print(solution_02([0, 0, 0, 0, 0, 0], [31, 10, 45, 1, 6, 19]))



def solution_03(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]