def jos(n, k):
    if n == 1:
        return 0
    else:
        return (jos(n - 1, k) + k) % n


print(jos(5, 3))
