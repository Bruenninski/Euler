def main():
    number = 2**1000
    sum = 0
    while number > 0:
        print("number: " + str(number))
        print("sum: " + str(sum))
        sum += number % 10
        number = number//10
    print(sum)


if __name__ == '__main__':
    main()
