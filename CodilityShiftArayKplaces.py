def solution(A, K):
    # write your code in Python 3.6
    def reverse(start, end, array):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

    start = 0
    end = len(A) - 1
    if len(A) == 0 or not A:
        return A
    if len(A) == 1 or K == 0:
        return A
    K %= len(A)
    reverse(start, end, A)
    reverse(start, K - 1, A)
    reverse(K, end, A)
    return A