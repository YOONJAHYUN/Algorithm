import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    n, number = input().split()
    numbers = []
    n = int(n)

    numbers.extend(number)
    i = 1

    while i != len(numbers):

        if numbers[i-1] == numbers[i]:
            numbers.pop(i-1)
            numbers.pop(i - 1)
            i = 1
        else:
            i += 1


    print(f'#{tc}', ''.join(numbers))