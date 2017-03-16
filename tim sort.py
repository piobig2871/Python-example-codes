from bisect import bisect_left

def tim_sort(T):
    for i in range(1, len(T)):
        val = T.pop(i)
        T.insert(bisect_left(T, val, 0, i), val)
    return T


print(tim_sort([5,4,3,2,1]))
