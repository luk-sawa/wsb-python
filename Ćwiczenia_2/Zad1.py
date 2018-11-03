def counting(begin, end, step):
    number = begin
    count = 0
    while number <= end:
        print(number)
        number += step
        count += 1
    print('There was ', count, " numbers")


first = int(input('Please enter first number: '))
last = int(input('Please enter last number: '))
stepping = int(input('Please enter step: '))
counting(first, last, stepping)
