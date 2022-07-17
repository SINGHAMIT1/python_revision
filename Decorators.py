import time


def cal_square(num):
    start = time.time()
    result = []
    for i in num:
        result.append(i * i)
    end = time.time()
    print("time required for squaring :", str((end - start) * 1000) + " mili seconds")
    return result


def cal_cube(nums):
    start = time.time()
    result = []
    for j in nums:
        result.append(j * j * j)
    end = time.time()
    print("time required for cubing :", str((end - start) * 1000) + " mili seconds")

    return result


array = range(1, 100)
print(cal_square(array))
print(cal_cube(array))
