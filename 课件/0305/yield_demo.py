def foo():
    for i in range(5):
        # return i
        yield i
res = foo()
print(res)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))