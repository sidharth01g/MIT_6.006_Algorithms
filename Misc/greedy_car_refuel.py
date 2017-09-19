def get_min_refuels(x, capacity):
    count = 0
    last_refuel = 0
    current = 0

    while True:
        while (current < len(x) - 1
               and (x[current + 1] - x[last_refuel] <= capacity)):
            current += 1

        if current == last_refuel:
            print('Cannot reach destination with current capacity ', capacity)
            return None

        if current < len(x) - 1:
            last_refuel = current
            print(
                'Refuel at station: ', last_refuel,
                ' at distance ', x[last_refuel])
            count += 1

        if current == len(x) - 1:
            return count


def main():
    x = [0, 21, 59, 68, 82, 93, 109, 125]
    x = [0, 30, 41]
    c = 40
    print('Fuel station distances: ', x)
    print('Min refuls: ', get_min_refuels(x, c))


if __name__ == '__main__':
    main()
