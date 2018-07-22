n = int(input())
items_dict = {}

for i in range(0,n):
    temp_list = []
    temp_items_list = {}
    inp_line = input()
    temp_list = inp_line.split(" -> ")
    temp_items_list = temp_list[1].split(",")
    if temp_list[0] in items_dict.keys():
        items_dict[temp_list[0]] = items_dict[temp_list[0]] + "," + temp_list[1]
    else:
        items_dict[temp_list[0]] = temp_list[1]

inp_clothing_item = input().split(" ")

for color, item_lst in items_dict.items():
    print(f"{color} clothes:")
    temp_list = []
    temp_list = item_lst.split(",")
    temp_dict = {}
    for i in range(0, len(temp_list)):
        if temp_list[i] in temp_dict.keys():
            temp_dict[temp_list[i]] += 1
        else:
            temp_dict[temp_list[i]] = 1

    for item, count in temp_dict.items():
        #temp_clothing_item = color + " " + item
        found_str = ""
        if inp_clothing_item[0] == color and inp_clothing_item[1] == item:
            found_str = " (found!)"
        print(f"* {item} - {count}{found_str}")