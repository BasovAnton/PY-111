from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    print(stairway)

    return direct_stairway_path(stairway)


def direct_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """прямой метод расчета"""
    #stairway # цены на ступени
    count_stairs = len(stairway)
    total_cost = [float("inf")]*count_stairs # стоимость перемещения по ступеням

    total_cost[0] =stairway[0] # начальные условия для первой ступени
    total_cost[1] = min(stairway[1], stairway[0]+stairway[1]) #начальные условия для второй ступени

    # i - цены ступени + min (стоимость i-1, стоимость i-2)
    for i in range(2, count_stairs): #len(stairway)
        total_cost[i] = stairway[i] + min(total_cost[i-1],total_cost[i-2])
    return  total_cost[-1] #total_cost[count_stairs]