import random


def sort():
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for pair in range(len(numbers)-1):
            if numbers[pair+1] < numbers[pair]:
                numbers[pair+1], numbers[pair] = numbers[pair], numbers[pair+1]
                is_sorted = False


numbers =[]
for number in range(50):
    numbers.append(random.randint(0, 100))
sort()
print(numbers)
isLists = True
for i in range(len(numbers)):
    if numbers[i] != sorted(numbers)[i]:
        print(numbers[i]+" "+sorted(numbers)[i])
        isLists = False
if isLists:
    print("sortowanie się zgadza")
else:
    print("sortowanie się niezgadza")
