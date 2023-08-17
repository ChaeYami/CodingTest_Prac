def solution(survey, choices):
    survey_count={"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for i,s in enumerate(survey):
        # if (choices[i]-4)>0:
        #     survey_count[[0]]
        #     s[1]
        if choices[i] <= 4:
            # 예) MJ에서 2(비동의)라면 M 2점
            survey_count[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            # 예) MJ에서 5(약간동의)라면 J 1점
            survey_count[survey[i][1]] += choices[i] - 4

    answer = ''
    if survey_count['R'] >= survey_count['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if survey_count['C'] >= survey_count['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if survey_count['J'] >= survey_count['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if survey_count['A'] >= survey_count['N']:
        answer += 'A'
    else:
        answer += 'N'


    return answer


#========================
def solution(survey, choices):
    survey_count={"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for i,s in enumerate(survey):
        if (choices[i]-4) >= 0:
            survey_count[s[1]] += (choices[i]-4)
        else:
            survey_count[s[0]] += abs(choices[i]-4)
    answer = ''
    answer += "R" if survey_count["R"]>=survey_count["T"] else "T"
    answer += "C" if survey_count["C"]>=survey_count["F"] else "F"
    answer += "J" if survey_count["J"]>=survey_count["M"] else "M"
    answer += "A" if survey_count["A"]>=survey_count["N"] else "N"
    return answer



# ========예제 테스트===================



survey1 = ["AN", "CF", "MJ", "RT", "NA"]
choices1 = [5, 3, 2, 7, 5]
# "TCMA"

survey2 = ["TR", "RT", "TR"]
choices2 =[7, 1, 3]
# "RCJA"

print("TCMA",solution(survey1, choices1))
print("RCJA",solution(survey2, choices2))