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

        # print(dice_numbers, '인 경우', 'A :', A_score, 'B:',B_score)

        win =  sum(1 for x, y in zip(A_score, B_score) if x > y)

        # win = 0
        # for a, b in zip(A_score, B_score):
        #     if a > b:
        #         win += 1
        # print('승',win)

        probability = win / len(A_score)

        # win = 0
        # total = 0

        # for case in product([0,1], repeat =len(A_score)):
        #     total += 1
        #     for i in range(len(A_score)):
        #         if case[i] == 1 and A_score[i] <= B_score[i]:
        #             break

        #         else:
        #             win +=1
        # probability = win / total

        pro_dic[dice_numbers] = probability

    for dice_numbers in pro_dic:
        if pro_dic[dice_numbers] == max(pro_dic.values()):
            answer.append(dice_numbers)
    answer = answer[0]

    # print(pro_dic)

    return answer