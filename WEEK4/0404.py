def solution(array):
    count_dict = {}  # 각 원소의 숫자와 갯수를 딕셔너리에 key와 value로 저장할 빈 딕셔너리!
    for num in array:
        # dict 키를 판별, 없으면 밸류가 1 , 있으면 밸류가 +1
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    # 등장횟수(value) 최댓값, 즉 value값이 제일 큰 key값을 return 해줘야 한다!
    max_count = max(count_dict.values())
    # 최빈값==mode 최빈값(key)을 반복문을 돌려 빈리스트에 담아서, 하나인지 여러개인지 판별해야 한다!
    mode_list = []
    for key, num in count_dict.items():
         if num == max_count:
             mode_list.append(key)
    # 리스트의 길이를 비교하여 최빈값의 갯수를 판별!
    if len(mode_list) == 1:
        return mode_list[0]
    else:
        return -1

d