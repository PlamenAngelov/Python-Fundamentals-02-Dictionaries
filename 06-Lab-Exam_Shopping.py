inp_string = input()
stock_dict = {}

while inp_string != "shopping time":
    temp_list = []
    temp_list = inp_string.split()[1:]
    key = temp_list[0]
    value = int(temp_list[1])

    if key in stock_dict.keys():
        stock_dict[key] += value
    else:
        stock_dict[key] = value
    inp_string = input()



inp_string = input()

while inp_string != "exam time":
    temp_list = []
    temp_list = inp_string.split()[1:]
    key = temp_list[0]
    value = int(temp_list[1])

    if key in stock_dict:
        if stock_dict[key] == 0:
            print(f"{key} out of stock")
        elif stock_dict[key] != 0:
            if value > stock_dict[key]:
                stock_dict[key] = 0
            else:
                stock_dict[key] -= value
    else:
        print(f"{key} doesn't exist")
    inp_string = input()


for key in stock_dict.keys():
    if stock_dict[key] > 0:
        print(f"{key} -> {stock_dict[key]}")