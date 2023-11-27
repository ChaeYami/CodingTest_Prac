from itertools import combinations
from itertools import permutations
from itertools import product

def calculate_score(*dice_list):
    score= []
    for combination in product(*dice_list[0]):
        score.append(sum(combination))
    return score


def solution(dice):
    answer = []
    n = len(dice)

    pro_dic = {}
    for dice_numbers in combinations(range(1, n + 1), n // 2):
        A_dice = [dice[i - 1] for i in dice_numbers]
        B_dice = [dice[i - 1] for i in set(range(1, n + 1)) - set(dice_numbers)]
        A_score = calculate_score(A_dice)
        B_score = calculate_score(B_dice)


        win =  sum(1 for x, y in zip(A_score, B_score) if x > y)


        probability = win / len(A_score)


        pro_dic[dice_numbers] = probability

    for dice_numbers in pro_dic:
        if pro_dic[dice_numbers] == max(pro_dic.values()):
            answer.append(dice_numbers)
    answer = answer[0]

    # print(pro_dic)

    return answer