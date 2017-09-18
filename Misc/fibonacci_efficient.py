def fib(n):
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return c


def main():
    while(True):
        try:
            x = int(input("Number ('q' to quit): "))
        except Exception as e:
            print('Error: ', str(e))
            continue
        if x == 'q':
            print('Invalid input. Returning')
            return
        print('Fibonacci: ', fib(x), '\n')


if __name__ == '__main__':
    main()
