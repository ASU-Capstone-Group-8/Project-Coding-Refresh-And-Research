# Advanced Level Concepts

# src/advanced/decorators_context_managers.py

from functools import wraps
import time


# Example of a custom decorator

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result

    return wrapper


@timing_decorator
def long_running_function():
    time.sleep(2)
    return "Finished"


# Example of a custom context manager

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


if __name__ == "__main__":
    print(long_running_function())

    with FileManager("example.txt", "w") as f:
        f.write("This is an example using a custom context manager.")