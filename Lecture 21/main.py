# import time
#
# def func1():
#     time.sleep(5)
#     print("Task 1 done")
#
# def func2():
#     time.sleep(3)
#     print("Task 2 done")
#
# def func3():
#     time.sleep(4)
#     print("Task 3 done")
#
# start_time = time.perf_counter()
#
# func1()
# func2()
# func3()
#
# end_time = time.perf_counter()
#
# print(f"Total time taken: {end_time - start_time}")

# import threading
#
# import time
#
# def func1():
#     time.sleep(5)
#     print("Task 1 done")
#
# def func2():
#     time.sleep(3)
#     print("Task 2 done")
#
# def func3():
#     time.sleep(4)
#     print("Task 3 done")
#
# start_time = time.perf_counter()
#
# thread1 = threading.Thread(target=func1)
# thread2 = threading.Thread(target=func2)
# thread3 = threading.Thread(target=func3)
#
# thread1.start()
# thread2.start()
# thread3.start()
#
# thread1.join()
# thread2.join()
# thread3.join()
#
# end_time = time.perf_counter()
#
# print(f"Total time taken: {end_time - start_time}")


# import time, threading
#
# def print_task(name):
#     print(f"Task {name} started")
#     time.sleep(3)
#     print(f"Task {name} completed")
#
# start_time = time.perf_counter()
#
# threads = []
#
# for i in range(1, 1001):
#     thread = threading.Thread(target=print_task, args=(i,))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
#
# end_time = time.perf_counter()
#
# print(f"Total time taken: {end_time - start_time}")


# import time, threading
# from concurrent.futures import ThreadPoolExecutor
#
# def print_task(name):
#     time.sleep(1)
#     print(f"Task {name} done")
#
# start_time = time.perf_counter()
#
# with ThreadPoolExecutor(max_workers=2000) as executor:
#     for i in range(1, 10001):
#         executor.submit(print_task, i)
#
#
# end_time = time.perf_counter()
#
# print(f"Total time taken: {end_time - start_time}")


import time
from concurrent.futures import ThreadPoolExecutor

def print_task(name):
    time.sleep(1)
    return f"Task {name} done"


start_time = time.perf_counter()

with ThreadPoolExecutor(max_workers=50) as executor:
    threads = [executor.submit(print_task, name=i) for i in range(1, 101)]

    for thread in threads:
        print(thread.result())

end_time = time.perf_counter()

print(f"Total time taken: {end_time - start_time}")












