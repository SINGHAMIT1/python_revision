def remote_control_next():
    yield "cnn"
    yield "espn"


itr = remote_control_next()
itr
print(next(itr))
print(next(itr))
for c in remote_control_next():
    print(c)


# fibonacci number using generator
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for f in fib():
    if f > 100:
        break
    print(f)

# using generator over class based iterator
# no need to define iter or next method
# no need to raise stopIteration exception. It will automatically generate
