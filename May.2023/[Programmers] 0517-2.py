#직사각형의 넓이 구하기
def solution(dots):
    answer = 0
    x_list = [dot[0] for dot in dots]
    y_list = [dot[1] for dot in dots]
    가로 = max(x_list) - min(x_list)
    세로 = max(y_list) - min(y_list)
    answer = 가로 * 세로
    #그 꼭짓점들의 x값-x값, y값-y값으로 밑변과 높이를 구한 후 곱하기
    # a = dots[0][0]-dots[1][0]
    # b = dots[1][1]-dots[2][1]
    # answer = abs(a*b) 처음해봤던 식
    return answer