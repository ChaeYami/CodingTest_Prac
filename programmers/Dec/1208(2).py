# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    x_size = []
    y_size = []

    for size in sizes:
        x_size.append(max(size))
        y_size.append(min(size))

    answer = max(x_size) * max(y_size)
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))