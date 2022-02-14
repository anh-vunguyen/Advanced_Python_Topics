def minimumBribes(q):
    total_bribes = 0
    no_people = len(q)
    # return to 0-based index
    q = [x - 1 for x in q]
    for i, p in enumerate(q):
        if p - i > 2:
            print('Too chaotic')
            return
        for j in range(max(p-1, 0), i):
            if q[j] > p:
                total_bribes += 1
    print(str(total_bribes))



q = [2, 1, 5, 3, 4]
minimumBribes(q)
q = [2, 5, 1, 3, 4]
minimumBribes(q)
q = [1, 2, 5, 3, 7, 8, 6, 4]
minimumBribes(q)
