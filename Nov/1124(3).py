def solution(gems):
    answer = [1, len(gems)]
    

    gems_dict = {}
    
    start = 0
    end = 1
    standard_gem = gems[start] # "DIA"
    gems_dict[gems[start]] = start # {"DIA" : 'start'}
    
    if len(set(gems)) == 1:
        return [1, 1]
    
    while end < len(gems):
        gems_dict[gems[end]] = end 
        # 1 -> {"DIA" : 0, "RUBY" : 1} / 2->{'DIA': 0, 'RUBY': 2} / 3 -> {"DIA" : 3, "RUBY" : 2}

        if standard_gem == gems[end]: # start와 end가 같으면 
            standard_gem = sorted(gems_dict.keys(), key=lambda x: gems_dict[x])[0]
            start = gems_dict[standard_gem]

        if len(gems_dict.keys()) == len(set(gems)): # 보석의 종류 (중복제거)
            current_answer = [start+1, end+1]

            if answer[1] - answer[0] > end - start:
                answer = current_answer
        
        end += 1

        
    return answer
    
    
solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])