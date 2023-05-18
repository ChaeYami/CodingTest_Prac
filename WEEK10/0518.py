
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

    temp_dict = {}
    time_dict = {}
    for record in records:
        time,number,status = record.split()
        hour,minute = time.split(':')
        minutes = int(hour)*60 + int(minute)

        if status == 'IN':
            temp_dict[number] = minutes
        elif status == 'OUT':
            time = minutes - temp_dict[number]
            if number in time_dict:
                time_dict[number] += time
            else:
                time_dict[number] = time
            del(temp_dict[number])
                
    for number, val in temp_dict.items():
        time = 1439 -val
        if number in time_dict:
            time_dict[number] += time
        else:
            time_dict[number] = time
            
    for number, time in time_dict.items():
        over_time = max(0, time-fees[0])
        total_fees = fees[1] + math.ceil(over_time/fees[2]) * fees[3]
        time_dict[number] = total_fees
    time_dict = sorted(time_dict.items())

    for number, fee in time_dict:
        answer.append(fee) 
        
    return answer   
       
        
    #     창호 튜터님 탄신일
    #    주차시간 = {}
    # for record in records:
    #     차량,시각, 방향 = record.split(" ")
    #     if 차량 not in 주차시간:
    #         주차시간[차량] = []
    #     주차시간[차량].append({"시각": 시각, "방향": 방향})
    #     hour,minute = 시간.split(':')
    #     minutes = int(hour)*60 + int(minute)
    # 누적 주차 시간 = 0
        # if status == 'OUT':
        # if 'IN':
            # 누적 주차 시간 = out 시간 - in 시간
        # else:
        #     누적 주차 시간 = minutes + 1


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