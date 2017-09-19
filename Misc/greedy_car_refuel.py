def get_min_refuels(x, capacity):
    print('len: ', len(x))
    count = 0
    last_refuel = 0
    current = 0

    while True:
        while (current < len(x) - 1
               and (x[current + 1] - x[last_refuel] <= capacity)):
            print(current)
            current += 1

        if current == last_refuel:
            return None

        if current < len(x) - 1:
            last_refuel = current
            print('  ', last_refuel)
            count += 1

        if current == len(x) - 1:
            return count


def main():
    x = [0, 21, 59, 68, 82, 93, 109, 125]
    c = 40
    print('Min refuls: ', get_min_refuels(x, c))


if __name__ == '__main__':
    main()
