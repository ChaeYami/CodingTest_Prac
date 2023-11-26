def distance_func(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                for x in range(5):
                    for y in range(5):
                        if place[x][y] == 'P' and (abs(i - x) + abs(j - y)) <= 2:
                            # 맨해튼 거리가 2 이하이면서 사이에 파티션이 없는 경우 거리두기 위반
                            if i == x and abs(j - y) == 2 and place[i][min(j, y) + 1] != 'X':
                                return False
                            elif abs(i - x) == 2 and j == y and place[min(i, x) + 1][j] != 'X':
                                return False
                            elif abs(i - x) == 1 and abs(j - y) == 1:
                                # 대각선 상에 있는 경우
                                if place[i][y] != 'X' or place[x][j] != 'X':
                                    return False
                # 대기실 내부에서의 거리두기 확인
                if i > 0 and place[i - 1][j] == 'P':
                    return False
                if j > 0 and place[i][j - 1] == 'P':
                    return False
                if i < 4 and place[i + 1][j] == 'P':
                    return False
                if j < 4 and place[i][j + 1] == 'P':
                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        if distance_func(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

solution(places)