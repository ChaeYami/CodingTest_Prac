# https://school.programmers.co.kr/learn/courses/30/lessons/159994

'''
1. goal[0] 과 cards1[0] 을 비교한다. 
1-1.같으면 둘 다 pop
1-2.다르다면 goal[0] 과 cards1[1] 을 비교한다. 
1-3.같으면 역시 둘 다 pop 
1-4 다르다면 No 반환 
2. 넘어갔다면 goal[0]로 반복 (삭제했으므로)

또한 list로 pop(0) 하면 리스트 길이만큼 시간이 걸리므로
모든 리스트를 deque로 변환한후 popleft 하는 것이 빠름
'''

from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    cards1_deq = deque(cards1)
    cards2_deq = deque(cards2)
    while answer!='No' and goal:
        word = goal[0]
        
        if cards1_deq != deque([]) and cards1_deq[0] == word:
            cards1_deq.popleft()
            goal.remove(word)
            
        elif cards2_deq != deque([]) and cards2_deq[0] == word:
            cards2_deq.popleft()
            goal.remove(word)
            
        else:
            answer = 'No'
        
    if goal == []:
        answer = 'Yes'
    return answer


cards1=["i", "drink", "water"]
cards2=["want", "to"]
goal=["i", "want", "to", "drink", "water"]
# result="Yes"
	
 
# cards1=["i", "water", "drink"]
# cards2=["want", "to"]
# goal=["i", "want", "to", "drink", "water"]		
# "No"

solution(cards1, cards2, goal)



'''
다른 사람 풀이

def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"

'''