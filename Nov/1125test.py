from itertools import combinations
from itertools import product

def calculate_score(*dice_list):
    score= []
    # print(*dice_list[0])
    for combination in product(*dice_list[0]):
        score.append(sum(combination))
    return score


def solution(dice):
    n = len(dice)

    for dice_numbers in combinations(range(1, n + 1), n // 2):
        A_dice = [dice[i - 1] for i in dice_numbers]
        B_dice = [dice[i - 1] for i in set(range(1, n + 1)) - set(dice_numbers)]
        A_score = calculate_score(A_dice)
        B_score = calculate_score(B_dice)
        # print(A_dice)
        print(A_score)
        win =  sum(1 for x, y in zip(A_score, B_score) if x > y)
        probability = win / len(A_score)
        if probability > 0.5 :
            print('n',dice_numbers)
