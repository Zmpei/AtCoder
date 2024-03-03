def func1(n):
    if n == 1:
        return 1
    return 2 * func1(n-1)


N = 10
for i in range(1, N+1):
    print(func1(i))

    
def func2(n):
    if n <= 3:
        return 1
    return func2(n-1) + func2(n-2) + func2(n-3)


N = 10
for i in range(1, N+1):
    print(func2(i))