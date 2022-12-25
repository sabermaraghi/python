n = int(input('Please enter an Integer number: '))
for x in range(1, n + 1):
    print('*' * x)
for y in range(n - 1, 0, n + 1):
    print('*' * y)