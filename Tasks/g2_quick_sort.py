# from typing import List
# from random import choice
#
#
# def sort(container: List[int]) -> List[int]:
#     """
#     Sort input container with quick sort
#
#     :param container: container of elements to be sorted
#     :return: container sorted in ascending order
#     """
#     if not container:
#         return container
#
#     pivot = choice(container)
#
#     return sort([v for v in container if v < pivot]) \
#         + [v for v in container if v == pivot] \
#         + sort([v for v in container if v > pivot])

from typing import List
from random import randint


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    def _sort(left_border, right_border) -> None:
        if left_border >= right_border:
            return
        random_index = randint(left_border, right_border)
        pivot = container[random_index]

        i, j = left_border, right_border

        while i <= j:
            while container[i] < pivot:
                i += 1
            while container[j] > pivot:
                j -= 1
            if i <= j:
                # взаимообмен
                container[i], container[j] = container[j], container[i]
                i += 1
                j -= 1
        _sort(left_border, j)
        _sort(i, right_border)

    _sort(0, len(container)-1)
    return container
