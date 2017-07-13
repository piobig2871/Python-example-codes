

def flawiusz(n, k=2):
    if n == 1:
        return 1
    return (flawiusz(n-1, k) + k-1) % n + 1

print(flawiusz(10))
