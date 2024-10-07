# src/advanced/multiprocessing_threading.py

import multiprocessing
import threading
import time


# Example of using threading

def thread_task(name):
    print(f"Thread {name} starting")
    time.sleep(1)
    print(f"Thread {name} finished")


# Example of using multiprocessing

def process_task(name):
    print(f"Process {name} starting")
    time.sleep(2)
    print(f"Process {name} finished")


if __name__ == "__main__":
    # Using threading
    threads = []
    for i in range(3):
        thread = threading.Thread(target=thread_task, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Using multiprocessing
    processes = []
    for i in range(2):
        process = multiprocessing.Process(target=process_task, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()