def task5():
    way_list = list(map(str, str(input())))
    x, y = 0, 0
    switcher_x = {
        "R": 1,
        "L": - 1
    }
    switcher_y = {
        "U": 1,
        "D": - 1
    }

    for direction in way_list:
        x += switcher_x.get(direction) or 0
        y += switcher_y.get(direction) or 0

    if (x == 0) and (y == 0):
        print("True")
    else:
        print("False")


task5()
