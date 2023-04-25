def fun(n):
    # base condition
    if n == 0:
        return
    print(n)
    fun(n-1)
    print(n)
fun(3)
