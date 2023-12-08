# https://school.programmers.co.kr/learn/courses/30/lessons/67256

'''
def solution(numbers, hand):
    answer = ''
    num_dict = {1:(3,0), 2:(3,1), 3:(3,3),
               4:(2,0), 5:(2,1), 6:(2,2), 
               7:(1,0), 8:(1,1), 9:(1,2), 
               '*': (0,0), 0:(0,1), '#': (0,2)}
    
    current_left = '*'
    current_right = '#'
    
    def distance_func(now,hand):
        dis = abs( (num_dict[now][0] - num_dict[hand][0])) + abs((num_dict[now][1] - num_dict[hand][1]) ) 
        return dis
    for i in numbers:
        if i in [1,4,7]:
            answer += "L"
            current_left = i
        elif i in [3,6,9]:
            answer += "R"
            current_right = i
        elif i in [2,5,8,0]:
            if distance_func(i,current_left) < distance_func(i,current_right) :
                answer += "L"
                current_left = i
            elif distance_func(i,current_left) > distance_func(i,current_right) :
                answer += "R"
                current_right = i            
            
            elif distance_func(i,current_left) ==  distance_func(i,current_right) and hand == 'right':
                answer += "R"
                current_right = i  
            elif distance_func(i,current_left) ==  distance_func(i,current_right) and hand == 'left':
                answer += "L"
                current_left = i
    print(answer)
                
    return answer
'''

def solution(numbers, hand):
    answer = ''
    num_dict = {1: (3, 0), 2: (3, 1), 3: (3, 2),
                4: (2, 0), 5: (2, 1), 6: (2, 2),
                7: (1, 0), 8: (1, 1), 9: (1, 2),
                '*': (0, 0), 0: (0, 1), '#': (0, 2)}

    def distance_func(hand_pos, target_pos):
        return abs(hand_pos[0] - target_pos[0]) + abs(hand_pos[1] - target_pos[1])

    current_left = '*'
    current_right = '#'

    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            current_left = i
        elif i in [3, 6, 9]:
            answer += "R"
            current_right = i
        elif i in [2, 5, 8, 0]:
            left_distance = distance_func(num_dict[current_left], num_dict[i])
            right_distance = distance_func(num_dict[current_right], num_dict[i])

            if left_distance < right_distance or (left_distance == right_distance and hand == 'left'):
                answer += "L"
                current_left = i
            else:
                answer += "R"
                current_right = i

    print(answer)
    return answer


