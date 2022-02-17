def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    print(n)
    return 0


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    a = 0
    b = 1
    if n == 1:
        return  a
    if n == 2:
        return b
    for _ in range(2, n):
        a, b = b, a + b

def fib_generator()
