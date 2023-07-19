import os
os.system("cls")
# 팀 구성 리스트 초기화
team = ["서채연", "이준영", "이정현", "배현아", "노탁근"]
navi_list = []
obs_list = []
driver_list = []
# 옵저버 역할을 맡을 팀원 선택 (매일 한명씩 돌아가며)
obs_index = 0
# 14일간의 팀 구성 리스트 작성
for day in range(14):
# 팀 구성
    navi_list.append([team[(obs_index+1)%5], team[(obs_index+2)%5]])
    driver_list.append([team[obs_index], team[(obs_index+3)%5]])
    obs_list.append(team[(obs_index+4)%5])
    # 옵저버 인덱스 업데이트
    obs_index = (obs_index+1) % 5
# 결과 출력
print("14일간의 팀 구성 리스트:")
for day in range(14):
    print(f"[Day {day+1}] A조 : 네비게이터 {navi_list[day][0]} 드라이버 {driver_list[day][0]} / B조 : 네비게이터 {navi_list[day][1]} 드라이버 {driver_list[day][1]}, 옵저버 {obs_list[day]}")
    
    
    
