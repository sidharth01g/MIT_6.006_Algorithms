def gcd(a, b):
    assert(type(a) is int and type(b) is int and a > 0 and b > 0)
    divident = max(a, b)
    divisor = min(a, b)
    while True:
        remainder = divident % divisor
        if remainder == 0:
            return divisor
        divident = divisor
        divisor = remainder


def main():
    while(True):
        try:
            x = int(input("Number ('q' to quit): "))
            y = int(input("Number ('q' to quit): "))
            print('GCD: ', gcd(x, y))
        except Exception as e:
            print('Error: ', e)
            continue


if __name__ == '__main__':
    main()
