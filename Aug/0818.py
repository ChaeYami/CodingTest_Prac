# https://school.programmers.co.kr/learn/courses/30/lessons/172927

'''
picks -> dia, iron, stone
각 곡괭이 다섯번 쓰면 끝
** 피로도
1. 다이아
    다이아 : 1 
    철 : 1
    돌 : 1
2. 철
    다이아 : 5
    철 : 1 
    돌 : 1
3. 돌
    다이아 : 25
    철 : 5
    돌 : 1
    
다이아, 철, 돌 곡괭이의 순서로 쓰고
다이아를 먼저 캐고 남으면 철, 돌의 순서로 캐기

** 피로도 계산
다이아 25, 철 5, 돌1 로 치환하고
캘 때 광물/곡괭이
ex)
    다이아 곡괭이로 다이아 25/25 =1
    다이아 곡괭이로 철 5/25 
    철 곡괭이로 다이아 25/5 = 5
    돌 곡괭이로 다이아 25/1 = 25
    돌 곡괭이로 철 5/1 = 5
'''

'''
def solution(picks, minerals):
    answer = 0
    
    mineral_mapping = {
    "diamond": 25,
    "iron": 5,
    "stone": 1
    }
    # map(리스트 원소 각각을 인자로 실행될 함수, 리스트)
    # mineral_mapping[x] : x를 받아 mineral_mapping[x] 값을 반환, x = "diamond", "iron", "stone"
    new_minerals = list(map(lambda x: mineral_mapping[x], minerals)) 
    # ex [25, 25, 25, 5, 5, 25, 5, 1]
    if new_minerals == []:
        pass
    else:
        while picks[0] >0:
            i = 0
            while i<5:
                if new_minerals == []:
                    break
                else:
                    if new_minerals[0] / 25 >=1:
                        answer += int(new_minerals[0] / 25)
                    else:
                        answer += 1
                    i +=1
                    new_minerals.remove(new_minerals[0])
            picks[0]-=1
        while picks[0] == 0 and picks[1] >0 :
            i = 0
            while i<5:
                if new_minerals == []:
                    break
                else:
                    if new_minerals[0] / 5 >=1:
                        answer += int(new_minerals[0] / 5)
                    else:
                        answer += 1
                    i +=1
                    new_minerals.remove(new_minerals[0])
            picks[1]-=1
        
        while picks[0] == 0 and picks[1] == 0 and picks[2] > 0:
            i = 0
            while i<5:
                if new_minerals == []:
                    break
                else:
                    if new_minerals[0] >=1:
                        answer += int(new_minerals[0])
                    else:
                        answer += 1
                    i +=1
                    new_minerals.remove(new_minerals[0])
            picks[1]-=1
    
    return answer
'''

total_fatigue=[[1,1,1],[5,1,1],[25,5,1]]
res=1000000000
mineral_mapping = {
    "diamond": 0,
    "iron": 1,
    "stone": 2
    }
 
# DFS 
def dfs(idx, dia, iron, stone, minerals, fatigue):

    if idx >= len(minerals) or (not dia and not iron and not stone):
        global res
        res = min(res, fatigue)
        return
 
    d_fatigue = 0
    i_fatigue = 0
    s_fatigue = 0
    # 광물 5개 캐기
    for i in range(idx, min(idx+5, len(minerals))):
        d_fatigue += total_fatigue[0][mineral_mapping[minerals[i]]]
        i_fatigue += total_fatigue[1][mineral_mapping[minerals[i]]]
        s_fatigue += total_fatigue[2][mineral_mapping[minerals[i]]]
 
    # 다이아 캘 때
    if dia:
        dfs(idx+5, dia-1, iron, stone, minerals, fatigue+d_fatigue)
 
    # 철 캘 때
    if iron:
        dfs(idx+5, dia, iron-1, stone, minerals, fatigue+i_fatigue)
 
    # 돌 캘 때
    if stone:
        dfs(idx+5, dia, iron, stone-1, minerals, fatigue+s_fatigue)
 

def solution(picks, minerals):
    global res
    dfs(0, picks[0], picks[1], picks[2], minerals, 0)
    return res


picks1 = [1, 3, 2]
minerals1 = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
picks2 = [0, 1, 1]
minerals2 = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]

print(solution(picks1, minerals1)) # 12
print(solution(picks2, minerals2)) # 50