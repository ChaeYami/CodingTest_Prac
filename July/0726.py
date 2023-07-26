# https://school.programmers.co.kr/learn/courses/30/lessons/160586

'''
1. targets[0] 
1-1. targets[0] 의 문자열을 하나씩 돌면서 keymap[0] 의 문자열에 몇번째에 있는지 판별
1-2. targets[0] 의 문자열을 하나씩 돌면서 keymap[1] 의 문자열에 몇번째에 있는지 판별 
1-3. 을 keymap 의 길이만큼 반복하면서 -1이 아닐 경우에 리스트에 담는다.
1-4. 리스트의 최솟값을 반환해 answer 에 append 한다.
2. targets[1] 반복
3. 을 targets 의 길이만큼 반복
'''


'''def solution(keymap, targets):
    answer = []
    for target in targets:
        cnt_sum=0
        
        for alphabet in target:
            cnt_lst = []
            for key in keymap:
                cnt = key.find(alphabet)
                if cnt >= 0:
                    cnt_lst.append(cnt+1)
            # print(cnt_lst)
            if cnt_lst == []:
                cnt_lst.append(-1)
            cnt_sum += min(cnt_lst)
        # print(cnt_sum)
        answer.append(cnt_sum)
    
    # print(answer)
    return answer'''



def solution(keymap, targets):
    answer=[]
    key_dict = {}
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            char = keymap[i][j]
            if char not in key_dict:
                key_dict[char] =(j + 1)
            else:
                key_dict[char] = min(key_dict[char],(j + 1))
    
    for target in targets:
        sum=0
        for t in target:
            if t in key_dict:
                sum += key_dict[t]
            else:
                sum = -1
                break
        answer.append(sum)
    return answer

keymap1 = ["ABACD", "BCEFD"]
targets1 = ["ABCD","AABB"] # [9, 4]

keymap2 = ["AA"]
targets2 = ["B"] # [-1]

keymap3 = ["AGZ", "BSSS"]
targets3 = ["ASA","BGZ"] # [4, 6]

# print(solution(keymap1, targets1))
# print(solution(keymap2, targets2))
# print(solution(keymap3, targets3))

solution(keymap1, targets1)
solution(keymap2, targets2)
solution(keymap3, targets3)