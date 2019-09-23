def count_digits(n):
    digits = 0
    while n != 0:
        digits += 1
        n = n // 10
    return digits


def main():
    # the fist two numbers of the fibonacci numbers are 1 so we start with index 2
    fib_low = 1
    fib_high = 1
    index = 2
    while count_digits(fib_high) < 1000:
        (fib_high, fib_low) = (fib_high + fib_low, fib_high)
        index += 1
        if index % 100 == 0:
            print("index: " + str(index) + " number of digits: " + str(count_digits(fib_high)))
    print(index)


if __name__ == '__main__':
    main()
