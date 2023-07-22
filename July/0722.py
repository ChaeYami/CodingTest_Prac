# https://school.programmers.co.kr/learn/courses/30/lessons/178871

'''
얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.
'''

'''
players = ["mumu", "soe", "poe", "kai", "mine"]
각 인덱스 mumu=0 soe=1 poe=2 kai=3 mine=4
callings = ["kai", "kai", "mine", "mine"]
1. kai의 현재 인덱스 idx = players.index(kai) => players.index(callings[0])
1-1. 바로 앞 선수와 순서 바꾸기 players[idx-1] , players[idx] = players[idx] , players[idx-1]
2. 같은 것을 callings[1] 에서 반복 
3. for 문 사용 후 result = players
result = ["mumu", "kai", "mine", "soe", "poe"]

'''
'''
# 1차시도
def solution(players, callings):
    answer = []
    cnt = len(callings)
    for i in range(cnt):
        idx = players.index(callings[i])
        players[idx-1] , players[idx] = players[idx] , players[idx-1]
    answer = players
    return answer
'''
'''
1차시도 결과

테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.06ms, 10.3MB)
테스트 4 〉	통과 (0.95ms, 10.3MB)
테스트 5 〉	통과 (19.05ms, 10.5MB)
테스트 6 〉	통과 (72.05ms, 10.8MB)
테스트 7 〉	통과 (1890.31ms, 14.2MB)
테스트 8 〉	통과 (8264.93ms, 18.5MB)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.00ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
'''

'''
시간이 오래 걸리는 이유 : 
list.index() 메서드의 시간 복잡도는 O(n)이기 때문에, callings에 포함된 각 선수의 인덱스를 찾기 위해 players 배열을 반복적으로 검색해야 함.

해결 방법 : 
players 대신 딕셔너리를 사용하여 선수 이름을 키로, 해당 선수의 인덱스를 값으로 저장
O(1)의 시간 복잡도
'''

# 2차시도
def solution(players, callings):
    # 선수 이름과 인덱스를 저장하는 딕셔너리 생성
    player_indices = {player: idx for idx, player in enumerate(players)}
    
    for calling in callings:
        idx = player_indices[calling]
        players[idx-1] , players[idx] = players[idx] , players[idx-1]
        # 딕셔너리의 인덱스 업데이트
        player_indices[calling] = idx - 1
        player_indices[players[idx]] = idx
    answer = players
    return answer

'''
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.1MB)
테스트 4 〉	통과 (0.30ms, 10.4MB)
테스트 5 〉	통과 (1.63ms, 10.6MB)
테스트 6 〉	통과 (3.11ms, 10.7MB)
테스트 7 〉	통과 (17.81ms, 14.4MB)
테스트 8 〉	통과 (37.56ms, 18.9MB)
테스트 9 〉	통과 (85.07ms, 27.9MB)
테스트 10 〉	통과 (244.65ms, 56.7MB)
테스트 11 〉	통과 (726.85ms, 91.3MB)
테스트 12 〉	통과 (540.64ms, 91.5MB)
테스트 13 〉	통과 (637.26ms, 91.5MB)
테스트 14 〉	통과 (0.01ms, 9.98MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
'''


players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))


'''
인상깊은 풀이

'''