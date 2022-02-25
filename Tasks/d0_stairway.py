from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    total_costs = {
        # по ключу номер ступени, по значению минимальная стоимость
    }

    def lazy_stairway_path(stair_number):
        """рекурсивная функция, которая возвращает стоимости до stair_number ступени"""
        if stair_number in total_costs:
            return total_costs[stair_number]

        if stair_number == 0:
            total_costs[stair_number] = stairway[stair_number]  # сохранил в кеш
            return stairway[stair_number]  # из кэша

        if stair_number == 1:
            return stairway[stair_number]

        current_cost = stairway[stair_number] + min(lazy_stairway_path(stair_number-1),
                                                    lazy_stairway_path(stair_number-2))
        total_costs[stair_number] = current_cost
        return total_costs[stair_number]

    return lazy_stairway_path(len(stairway)-1)


def direct_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """прямой метод расчета"""
    # stairway, цены на ступени
    count_stairs = len(stairway)
    total_cost = [float("inf")]*count_stairs  # стоимость перемещения по ступеням

    total_cost[0] = stairway[0]  # начальные условия для первой ступени
    total_cost[1] = min(stairway[1], stairway[0]+stairway[1])  # начальные условия для второй ступени

    # i - цены ступени + min (стоимость i-1, стоимость i-2)
    for i in range(2, count_stairs):  # len(stairway)
        total_cost[i] = stairway[i] + min(total_cost[i-1], total_cost[i-2])
    return total_cost[-1]  # total_cost[count_stairs]


def reverse_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:

    count_stairs = len(stairway)
    total_cost = [float("inf")]*count_stairs  # стоимость перемещения по ступеням

    total_cost[0] = stairway[0]  # начальные условия для первой ступени
    total_cost[1] = stairway[1]  # начальные условия для второй ступени

    for i in range(0, count_stairs-2):
        total_cost[i + 1] = min(total_cost[i + 1], stairway[i + 1] + total_cost[i])
        total_cost[i + 2] = min(total_cost[i + 2], stairway[i + 2] + total_cost[i])

    total_cost[-1] = min(total_cost[-1], stairway[-1] + total_cost[-2])

    return total_cost[-1]
