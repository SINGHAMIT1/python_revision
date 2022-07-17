import time
import multiprocessing

squared_num = []


def cal_square(numbers):
    global squared_num
    for n in numbers:
        print("square : " + str(n * n))
        squared_num.append(n * n)
    print("All Squared Results :", squared_num)


# def cal_cube(numbers):
#     for n in numbers:
#         time.sleep(0.5)
#         print("cube : ", str(n * n * n))


if __name__ == "__main__":
    arr = [1, 3, 4, 5, 7]
    p1 = multiprocessing.Process(target=cal_square, args=(arr,))
    # p2 = multiprocessing.Process(target=cal_cube, args=(arr,))
    p1.start()
    # p2.start()

    p1.join()
    # p2.join()

    print("done !")


# sharing data between processes using array and value
import time
import multiprocessing


def cal_square(numbers, result, v):
    v.value=6.75

    for i,n in enumerate(numbers):
        result[i]=n*n


if __name__ == "__main__":
    arr = [1, 3, 4, 5, 7]
    result=multiprocessing.Array("i",5)
    v=multiprocessing.Value("d",0.0)
    p1 = multiprocessing.Process(target=cal_square, args=(arr,result,v))

    p1.start()

    p1.join()

    print(result)
    print(v.value)


# Sharing Data Between Processes Using Multiprocessing Queue
import time
import multiprocessing


def cal_square(num,q):
    for n in num:
        q.put(n * n)


if __name__ == "__main__":
    arr = [1, 3, 4, 5, 7]
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=cal_square, args=(arr, q))

    p1.start()

    p1.join()

    while q.empty() is False:
        print(q.get())
