deposit = int(input())
if deposit >= 50_000 and deposit <= 700_000:
    year = 0
    while deposit <= 700_000:
        year += 1
        deposit += deposit * 7.1 / 100
    print(year)
