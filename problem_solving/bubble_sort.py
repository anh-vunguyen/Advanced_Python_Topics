def countSwaps(a):
    n = len(a)
    swap = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]
                swap += 1
    print(f"Array is sorted in {swap} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

a = [6, 4, 1]
countSwaps(a)
