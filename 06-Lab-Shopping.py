def input_data(stopping_string):
    lst = []
    while True:
        data = input()
        data1 = data.split()[1:]
        if data == stopping_string:
            break
        else:
            lst.append(data1)
    return lst


def stock_the_shop(input_lst):
    dict = {}
    for item in input_lst:
        if item[0] in dict:
            dict[item[0]] += int(item[1])
        else:
            dict[item[0]] = int(item[1])
    return dict


shopping_time = stock_the_shop(input_data("shopping time"))
exam_time = input_data("exam time")


def order_from_shop(input_lst, stock_dict):
    for item in input_lst:
        stock_key = item[0]
        stock_value = int(item[1])
        if stock_key in stock_dict:
            if stock_dict[stock_key] == 0:
                print(f"{stock_key} out of stock")
            elif stock_dict[stock_key] != 0:
                if stock_dict[stock_key] < stock_value:
                    stock_dict[stock_key] = 0
                else:
                    stock_dict[stock_key] -= stock_value
        else:
            print(f"{stock_key} doesn't exist")
    for item in stock_dict:
        if stock_dict[item] > 0:
            print(f"{item} -> {stock_dict[item]}")


order_from_shop(exam_time, shopping_time)