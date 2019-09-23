import operator

numbers = {1: 1}


def main():
    for i in range(1000000):
        collatz(i)
        if i % 10000 == 0:
            print(i)
    maximum = max(numbers.items(), key=operator.itemgetter(1))[0]
    print(maximum)
    print("size: " + str(numbers[maximum]))


def collatz(initial):
    """ The collatz function it creates a "path" in the numbers dictionary by adding the known numbers there."""
    count: int = 0
    n = initial
    while n > 1:
        if n in numbers:
            numbers[initial] = numbers[n] + count
            return
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        count += 1
        if n == 1:
            numbers[initial] = count
            return


if __name__ == '__main__':
    main()
