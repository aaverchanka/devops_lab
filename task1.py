def task1():
    num_student = int(input())
    dict_student = {}
    for i in range(num_student):
        list_s = input().split(" ")
        marks = [float(item) for item in list_s[1:]]
        dict_student[list_s[0]] = (sum(marks)/len(marks))
    name_student = input()
    print(f'{dict_student[name_student]:.2f}')


task1()
