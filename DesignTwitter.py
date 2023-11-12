# from collections import defaultdict
# hm=defaultdict(int)
# print(type(hm))


def fib(n):
    fibfirst=0##zero
    fibsecond=1
    if n == fibfirst:
        return fibfirst
    elif n== fibsecond:
        return fibsecond
    for i in range(2, n+1):
        newsum=fibsecond+fibfirst
        fibfirst=fibsecond ##1
        fibsecond=newsum ### 1
    return newsum
print(fib(5))

##test fib 2=> 1 fib 3