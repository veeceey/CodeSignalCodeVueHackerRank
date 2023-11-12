def solution(A):
    # write your code in Python 3.6
    ##hashmap with key "value" and value = freq

    ##if freq <2 return

    hm = {}
    for num in A:
        hm[num] = 1 + hm.get(num, 0)
    for number, freq in hm.items():
        if freq % 2 == 1:
            return number
