inp_string = input()

my_dict = {}
while inp_string != "end":
    temp_list = []
    temp_list = inp_string.split(" = ")
    key = temp_list[0]
    value = temp_list[1]
    if value.isdigit():
        my_dict[key] = value
    else:
        if value in my_dict.keys():
            my_dict[key] = my_dict[value]
    inp_string = input()

for key, value in my_dict.items():
    print(f"{key} === {int(value)}")