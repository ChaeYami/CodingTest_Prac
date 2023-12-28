def solution(array):
    count_list = []
    count = []
    for l in array:
        if l in count_list:
            count[count_list.index(l)] += 1
        else:
            count_list.append(l)
            count.append(1)
    print(count_list)
    print(count)
    r = 0
    for a in count:
        if a == max(count):
            r += 1
        if r > 1:
            result = -1
            return result
    result = count_list[count.index(max(count))]
    return result





5:39
def solution(array):
    # count_list=[1,2,5,10] array중복값 제거
    # count=[0,0,0,0] count_list요소별 갯수 초기설정
    count_list = set(array)
    count = [0] * len(count_list)
    for l in array:  # array의 요소가 몇 번 기록되는지 세어주기위해 사용
        if l in count_list:
            count[count_list.index(l)] += 1
        else:
            count.append(1)
    print(count_list)
    print(count)
    r = 0  # 최빈값의 을 0으로 만들고 최대 갯수를 알기위해 사용
    for a in count:
        if a == max(count):  # 같은 숫자를 찾기위해 == 를 사용했다.
            r += 1  # 최댓값과 같은 값이 있으면
        if r > 1:   # 최빈값이 2개 이상일땐 더이상 돌릴필요가 없으므로 걸러주는if문.
            result = -1  # 걸려졌을때의 결과값은 -1
            return result  # 결과값 나왔으니 그놈을 solution함수의 output값 내보내기
    result = count_list[count.index(max(count))]
    return result