def zrange(a, b=0, c=1):
    if not b:
        a, b = b, a
    while a < b:
        yield a
        a += c

print(zrange(10))
print(zrange(10))
