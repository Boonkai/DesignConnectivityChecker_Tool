for i in range(2):
    print("Outer loop:", i)
    for j in range(3):
        if j == 1:
            continue
        print("Inner loop:", j)
        for k in range(3):
            if k == 2:
                continue
            print("Nested loop:", k)