# https://school.programmers.co.kr/learn/courses/30/lessons/161990

'''
1차시도
def solution(wallpaper):
    answer = []
    x_list = []
    y_list=[]
    for string in wallpaper:
        y = wallpaper.index(string) # 행 정렬
        x1 = string.find('#') # 해당 행의 첫 파일 위치 (드래그 시작)
        x2 = string.rfind('#')+1 # 해당 행의 마지막 파일 위치 (드래그 끝)
        if x1 != -1: # 파일이 있는 행에 대하여
            x_list.append(x1) #시작점
            x_list.append(x2) #끝점
            y_list.append(y)
            #오름차순 정렬
            x_list.sort() 
            y_list.sort()
    answer.append(y_list[0])
    answer.append(x_list[0])
    answer.append(y_list[-1]+1) # y좌표 드래그 끝
    answer.append(x_list[-1])
    return answer
    
이렇게 했는데 몇 테스트케이스에서 실패함

1. 'enumerate' 함수를 사용하여 'wallpaper' 리스트의 각 행의 인덱스와 값에 접근합니다.
2 'x_list'와 'y_list'의 정렬을 간단하게 하였으며, 'append' 연산이 순서를 보존하기 때문에 더욱 간편해졌습니다.
3. 'y_max'와 'y_list[-1]+1'의 계산을 합쳐 중복 계산을 피했습니다.
'''

def solution(wallpaper):
    answer = []
    x_list = []
    y_list = []
    for y, string in enumerate(wallpaper):
        x1 = string.find('#')  # 해당 행의 첫 '#' 문자 위치 (드래그 시작)
        x2 = string.rfind('#') + 1  # 해당 행의 마지막 '#' 문자 위치 (드래그 끝)
        if x1 != -1:
            x_list.append(x1)
            x_list.append(x2)
            y_list.append(y)
    if not x_list or not y_list:
        return []  # '#' 문자가 없는 경우 빈 리스트를 반환

    x_min = min(x_list)
    x_max = max(x_list)
    y_min = min(y_list)
    y_max = max(y_list) + 1  # y좌표 드래그 끝
    answer = [y_min, x_min, y_max, x_max]
    return answer

wallpaper1 = [".#...", "..#..", "...#."] #[0, 1, 3, 4]
wallpaper2 = ["..........", ".....#....", "......##..", "...##.....", "....#....."]	#[1, 3, 5, 8]
wallpaper3 = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]	#[0, 0, 7, 9]
wallpaper4 = ["..", "#."]	#[1, 0, 2, 1]
print(solution(wallpaper1))
print(solution(wallpaper2))
print(solution(wallpaper3))
print(solution(wallpaper4))