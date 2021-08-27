def fibonacci():
    f1 = 0
    f2 = 1
    yield f1
    yield f2
    fn_1 = f2
    fn_2 = f1
    while True:
        fn = fn_1 + fn_2
        yield fn
        fn_2 = fn_1
        fn_1 = fn


generator = fibonacci()
for i in range(5):
    print(next(generator))
