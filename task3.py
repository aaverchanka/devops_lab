number = int(input())


def task3(n):
    if n == 1:
        return 1
    else:
        return n * task3(n-1)


print(task3(number))
