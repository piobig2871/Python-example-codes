def my_int(number, system=10):
    '''INPUT:
    string of integers
    OUTPUT:
    Integer'''
    dictionary = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    ret = 0
    for idx, num in enumerate(str(number)[::-1]):
        ret += dictionary[num] * (system ** idx)
    return ret

print(my_int('123423342342342'))
