# Task 1

def show_line(symbol, function_to_call):
    function_to_call(symbol)


def print_line(symbol):
    for _ in range(10):
        print(symbol, end="")
    print()


def print_column(symbol):
    for _ in range(10):
        print(symbol)


print("\nPrint in one LINE")
show_line("#", print_line)
print("Print in one COLUMN")
show_line("#", print_column)

# Task 2
import time


def measure_time(func):
    def wrapper(number):
        start = time.perf_counter()
        result = func(number)
        end = time.perf_counter() - start
        print(f"Алгоритм виконано за {end:.6f} секунд")
        return result

    return wrapper


@measure_time
def calculate_sum(number):
    result = 0
    for i in range(0, number):
        result += i
    return result


print(calculate_sum(100000000))
