def solution(distance, rocks, n):
    # 시작과 끝의 최소 최대는 1, distance
    start = 1
    end = distance
    
    rocks.sort() # 이분탐색을 위해선 정렬되어있어야 함
    rocks.append(distance) # 바위부터 거리까지
    
    while start <= end:
        
        mid = (start+end)//2 # 자를 위치
        
        delete = 0 # 제거한 바위
        prev_rock = 0 # 이전 바위
        
        for rock in rocks:
            dist = rock - prev_rock # 바위 사이의 거리
            
            # 자를 위치보다 바위가 앞에 있으면 삭제
            if dist < mid:
                delete += 1
                if delete > n: 
                    break
            else:
                prev_rock = rock # 삭제 안 했으면 이전 바위 업데이트
                
        if delete > n: # 자를 위치가 너무 크면 삭제 횟수 초과
            end = mid -1
        else:
            answer = mid
            start = mid + 1
    return answer