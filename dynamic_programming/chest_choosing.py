green_path = []
green_money = []
green_chests = []

blue_path = []
blue_money = []
blue_chests = []

def best_chests(green_chest_list, blue_chest_list):
    assert(len(green_chest_list) == len(blue_chest_list))
    global green_path, green_money, green_chests, blue_path, blue_money, blue_chests
    green_chests = green_chest_list
    green_path = [-1] * len(green_chests)
    green_money = [-1] * len(green_chests)

    blue_chests = blue_chest_list
    blue_path = [-1] * len(blue_chests)
    blue_money = [-1] * len(blue_chests)

    green_option = best_dp(True, 0)
    blue_option = best_dp(False, 0)

    if green_option > blue_option:
        decode_choices(True)
        print(f"Total Money - {green_option}")
    else:
        decode_choices(False)
        print(f"Total Money - {blue_option}")


def best_dp(open_green, index) -> int:
    # print(f'Blue Path: {blue_path}\nGreen Path: {green_path}\nIndex: {index}')
    if open_green:
        if index == len(green_chests) - 1: # base case
            if green_chests[index] <= 0: # should we open the last case or not
                green_path[index] = -1
                green_money[index] = 0
                return 0
            green_path[index] = len(green_path) - 1
            green_money[index] = green_chests[index]
            return green_chests[index]
        # have we solved the current problem
        if green_money[index] != -1:
            return green_money[index]
        # compare options of opening this chest vs not
        open_current = green_chests[index] + best_dp(False, index+1)
        dont_open_current = best_dp(True, index+1)
        if open_current > dont_open_current: # should we open this case or wait for a future green case
            green_path[index] = index
            green_money[index] = open_current
        else:
            green_path[index] = green_path[index + 1]
            green_money[index] = green_money[index + 1]
        return green_money[index]
    else:
        if index == len(blue_chests) - 1: # base case
            if blue_chests[index] <= 0: # should we open the last case
                blue_path[index] = -1
                blue_money[index] = 0
                return 0
            blue_path[index] = len(blue_path) - 1
            blue_money[index] = blue_chests[index]
            return blue_chests[index]
        # have we solved the current problem
        if blue_money[index] != -1:
            return blue_money[index]
        # compare options of opening this chest vs not
        open_current = blue_chests[index] + best_dp(True, index+1)
        dont_open_current = best_dp(False, index+1)
        if open_current > dont_open_current: # should we open this case or wait for a future blue case
            blue_path[index] = index
            blue_money[index] = open_current
        else:
            blue_path[index] = blue_path[index + 1]
            blue_money[index] = blue_money[index + 1]
        return blue_money[index]

def decode_choices(is_green):
    index = 0
    on_green = is_green
    print("Should open - ", end="")
    while index < len(green_path):
        if on_green:
            if green_path[index] == -1:
                break
            print(f'Green Chest {green_path[index]+1}, ', end="")
            index = green_path[index] + 1
        else:
            if blue_path[index] == -1:
                break
            print(f'Blue Chest {blue_path[index]+1}, ', end="")
            index = blue_path[index] + 1
        on_green = not on_green
    print()

best_chests([8, 1, 4, 10, 2, 6, -4], [1, -1, -1, 3, 3, 10, -2])