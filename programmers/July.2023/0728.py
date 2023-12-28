# https://school.programmers.co.kr/learn/courses/30/lessons/150370




def time_convert(t) :
    year, month, day = map(int, t.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    term_dict = dict()
    today = time_convert(today)
    answer = []    
    
    for term in terms :
        name, period = term.split()
        term_dict[name] = int(period) * 28
    
    for idx, privacy in enumerate(privacies) :
        start, name = privacy.split()
        end = time_convert(start) + term_dict[name]
        if end <= today :
            answer.append(idx+1)    
    
    return answer


today1 = "2022.05.19"
terms1 = ["A 6", "B 12", "C 3"]
privacies1 = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# result [1, 3]

today2 = "2020.01.01"
terms2 = ["Z 3", "D 5"]
privacies2 = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
# result [1, 4, 5]
