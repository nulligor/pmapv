import operator
from concurrent.futures import ThreadPoolExecutor
from itertools import chain
from functools import reduce


def pmapv(f, arg):
    """Applies f(arg[0]), f(arg[1])... as a multi-threaded process"""

    accum = []
    with ThreadPoolExecutor() as exec:
        for _ in exec.map(f, arg):
            accum.append(_)
    try:
        return accum
    except:
        return []


def pflatmapv(f, arg):
    """
    Applies f(arg[0]), f(arg[1])... as a multi-threaded process
    and flattens its results
    """

    flatten = lambda l: reduce(operator.concat, l)
    accum = []
    with ThreadPoolExecutor() as exec:
        for _ in exec.map(f, arg):
            accum.append(_)
    try:
        return flatten(accum)
    except TypeError:
        return list(chain.from_iterable(accum))
    else:
        return []
