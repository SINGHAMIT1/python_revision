# map and reduce
def f(n):
    return n * n


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    result = []
    for n in array:
        result.append(f(n))
    print(result)

# map : divide the work/inputs between multiple cores is called map
# reduce: aggregate those individual core results in a single output called reduce
# same program by implementing map and reduce by Pool Class
from multiprocessing import Pool


def f(n):
    return n * n


if __name__ == "__main__":
    p = Pool()
    array = [1, 2, 3, 4, 5]

    result = p.map(f, array)
    print(result)

# comparing the performance between parallel and serial processing
import time
from multiprocessing import Pool


def f(n):
    sum = 0
    for i in range(1000):
        sum += i * i
    return sum


if __name__ == "__main__":
    t1 = time.time()  # current time
    p = Pool(processes=8)  # 8 core
    result = p.map(f, range(100000))
    p.close()
    p.join()

    print("Parallel Processing took time :", time.time() - t1)  # current time -starting time

    t2 = time.time()
    result = []
    for i in range(100000):
        result.append(f(i))
    print("Serial Processing took time :", time.time() - t2)

# using Pool will speed up your processing time
