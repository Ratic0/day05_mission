def get_odd():
    for i in range(10):
        if i % 2 == 0:
            pass
        else:
            yield i

count = 1
for i in get_odd() :
    if count == 3:
        print(i)
        break
    else:
        count += 1

