# src/advanced/generators_iterators.py

# Example of a custom iterator

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


# Example of a generator function

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    # Using the custom iterator
    for number in Counter(1, 5):
        print(number)

    # Using the generator
    for value in fibonacci_sequence(10):
        print(value)