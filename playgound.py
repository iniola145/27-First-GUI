def add(*args):
    a = 0
    for i in args:
        a += i
    print(type(a))
    print(a)


add(1, 2, 1, 2, 4, 10)
