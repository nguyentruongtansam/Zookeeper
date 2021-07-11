N = int(input())
if 1 <= N <= 100:
    i = 1
    fac_N = 1
    while i <= N:
        fac_N *= i
        i +=1
    print(fac_N)
