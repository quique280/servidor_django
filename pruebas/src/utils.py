from itertools import *

def replace(iter, pos, formulas):
    yield from islice(iter, 0, pos)
    yield from formulas
    yield from islice(iter, pos + 1, None)

def iterate(f, start=None):
    """ Yields start, f(start), f(f(start)), ... """
    next = start
    while True:
        yield next
        next =  f(next)

def first(iterable):
    """ Takes the first of iterable """
    for value in iterable:
        return value

def iFirst(iterable):
    """ Takes the first of iterable """
    for value in iterable:
        yield value
        return

def firstOccurrence(predicate, iterable):
    return next((x for x in iterable if predicate(x)), None)

def iFirstOccurrence(predicate, iterable):
    yield next((x for x in iterable if predicate(x)), None)

def firstAppliedNotNone(value, funcList):
    applied = (list(r(value)) for r in funcList)
    return first((y for y in applied if len(y) > 0))


if __name__ == "__main__":
    m = [0,1,2,3,4,5]
    rep = [666, 777]
    print(m, rep, list(replace(m, 0, rep)))