n = 0
for i in range(1900000):
    if n > 15:
        print(i)
    else:
        n = 0

    for index in range(i):
        if i != 0:
            n += 1/i
