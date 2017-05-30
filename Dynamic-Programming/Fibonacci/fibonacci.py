import time


def fibonacci_naive_recursive(n):
    """
    Return the nth Fibonacci number (int)
    """
    if n <= 2:
        return 1
    else:
        return (fibonacci_naive_recursive(n - 1) +
                fibonacci_naive_recursive(n - 2))

def fibonacci_dp(n, fib_dict=None):
    """
    Returns a dict containing all Fibonacci numbers from 0 to n
    """
    # print "n: %s" % str(n)

    if type(n) is not int:
        print("ERROR: Invalid type for number")
        return None

    if fib_dict is None:
        fib_dict = {}

    if n in fib_dict:
        return fib_dict

    if n <= 2:
        fib_dict[n] = 1
    else:
        fib_dict = fibonacci_dp(n - 2, fib_dict)
        fib_dict_2 = fibonacci_dp(n - 1, fib_dict)
        fib_dict.update(fib_dict_2)
        fib_dict[n] = fib_dict[n - 1] + fib_dict[n - 2]

    return fib_dict


def fibonacci_dp_bottom_up(n):
    """
    Returns the nth Fibonacci number
    """
    fibonacci = {}

    for i in range(1, n + 1):
        if i <= 2:
            fib = 1
        else:
            fib = fibonacci[i - 1] + fibonacci[i - 2]

        fibonacci[i] = fib

    return fibonacci[n]



n = 38

print("\nNaive execution:")
start_time = time.time()
print fibonacci_naive_recursive(n)
print("--- %s seconds ---" % (time.time() - start_time))


print("\nExecution using DP:")
start_time = time.time()
fib_dict = fibonacci_dp(n)
print fib_dict[n]
# print fib_dict
print("--- %s seconds ---" % (time.time() - start_time))


# Slightly faster than recursive DP
print("\nExecution using DP (bottom-up approach):")
start_time = time.time()
print fibonacci_dp_bottom_up(n)
print("--- %s seconds ---" % (time.time() - start_time))
