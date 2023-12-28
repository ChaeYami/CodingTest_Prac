
import math

'''
주차 요금 계산
주차 요금을 나타내는 정수 배열 fees, 
자동차의 입/출차 내역을 나타내는 문자열 배열 records
차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return
'''

# 1. 분류 - 완료
# 2. 주차시간 계산
# 3. 23:59 출차 적용
# 4. 요금 계산
# 5. 정렬

# 기본요금 + ((누적주차시간-기본시간)/단위시간)올림 * 단위요금
# 시간으로 나타내야 함,, 00시를 기준으로??? 분단위로? ex 05:34 5 * 60 + 34
# 출차시간 - 입차시간

def solution(fees, records):
    answer = []
    temp_dict = {} # 입, 출차 정보 담는 딕셔너리
    time_dict = {} # 해당 차의 주차시간을 담는 딕셔너리
    for record in records:
        time,number,status = record.split() # 시간 / 차 번호 / 입,출차여부
        hour,minute = time.split(':')
        minutes = int(hour)*60 + int(minute) # 00시 기준으로 분단위 시각

        if status == 'IN': # 입차일때
            temp_dict[number] = minutes # '차번호' : '분단위 시각'
        elif status == 'OUT': # 출차일때
            time = minutes - temp_dict[number] # 출차시각-입차시각을 시간 딕셔너리에 저장
            if number in time_dict:
                time_dict[number] += time # 기존 키값이 있다면 새 요소로 저장
            else:
                time_dict[number] = time # 기존에 없으면 초기화하면서 저장
            del(temp_dict[number]) # OUT 까지 완료되면 기존 딕셔너리에서 삭제
    # 출차 없을 때            
    for number, val in temp_dict.items(): # OUT되지 않은 차의 정보만 남은 딕셔너리
        time = 1439 -val # 23시59분 출차로 계산한다.
        if number in time_dict:
            time_dict[number] += time # 기존 키값이 있다면 새 요소로 저장
        else:
            time_dict[number] = time # 기존에 없으면 초기화하면서 저장
    # 주차비 계산        
    for number, time in time_dict.items(): 
        over_time = max(0, time-fees[0]) # 기본요금 초과시간
        total_fees = fees[1] + math.ceil(over_time/fees[2]) * fees[3] # 주차비 계산
        time_dict[number] = total_fees # 기존 시간 딕셔너리 사용해서 시간을 주차비로 업데이트
    time_dict = sorted(time_dict.items())

    for number, fee in time_dict:
        answer.append(fee) 
        
    return answer   
       
        



# 입출력 예
'''
fees : [180, 5000, 10, 600]
records : ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
result : [14600, 34400, 5000]
-----------------------------
fees : [120, 0, 60, 591]
records : ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]
[1, 461, 1, 10]	["00:00 1234 IN"]
result : [14841]
'''

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))