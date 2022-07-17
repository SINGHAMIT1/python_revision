# doing multiple tasks by the cpu without staying idle is called multithreading
import time
import threading


def cal_square(num):
    print("Calculate Square Numbers")
    for n in num:
        time.sleep(0.2)
        print("Square :", n * n)


def cal_cube(num):
    print("Calculate Cube Numbers")
    for n in num:
        time.sleep(0.2)
        print("Cube :", n * n * n)


arr = [1, 2, 3]
t1 = (threading.Thread(target=cal_square, args=(arr,)))
t2 = (threading.Thread(target=cal_cube, args=(arr,)))
# as (arr) is a tuple we need to give , here. like (arr,)
t = time.time()
t1.start()
t2.start()
t1.join()
t2.join()

print("Time Required :", t)
