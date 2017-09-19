def gcd(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    r = a % b
    return gcd(b, r)


def main():
    while(True):
        try:
            x = int(input("Number 1: "))
            y = int(input("Number 2: "))
            print('GCD: ', gcd(x, y))
        except Exception as e:
            print('Error: ', e)
            continue


if __name__ == '__main__':
    main()
