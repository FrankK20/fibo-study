def fib_rec(n):
    """
    A simple recursive implementation for calculating the n-th element
    of the fibonacci series. The fibonacci series is defined as:
            fib(0) = 1
            fib(1) = 1
            fib(n) = fib(n-2) + fib(n-1)
    :param n: int the index of the series element
    :return: int the value of the n-th element of the fibonacci series
    """
    assert (type(n) == int)
    if n < 0:
        raise ValueError('Wrong Input, n has to be a positive int')
    elif (n == 0) or (n == 1):
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_dic(n):
    """
    A better recursive implementation which utilizes a dictionary dic
    for saving known result, so the same calculations do not need to
    be done more then once
    :param n: int the index of the series element
    :return: int the value of the n-th element of the fibonacci series
    """
    dic = {}
    def fib(n):
        assert(type(n)==int)
        if n < 0:
            raise ValueError('Wrong Input, n has to be a positive int')
        elif (n == 0) or (n == 1):
            return 1
        elif n in dic.keys():
            return dic[n]
        else:
            dic[n] = fib(n - 1) + fib(n - 2)
            return dic[n]
    return fib(n)
