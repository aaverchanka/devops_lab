def task2():
    result_dict = {}
    arr1 = parser_to_int_array(input())
    arr2 = parser_to_int_array(input())
    for i in range(len(arr1)):
        if i > (len(arr2)-1):
            result_dict[arr1[i]] = None
        else:
            result_dict[arr1[i]] = arr2[i]
    print(result_dict)


def parser_to_int_array(string):
    words = string.split((" "))
    return [int(word) for word in words]


task2()
