inp_string = input()
my_dict = {}

while inp_string != "Over":
    temp_list = []
    temp_list = inp_string.split(" : ")
    key = temp_list[0]
    value = temp_list[1]

    if value.isdigit():
        my_dict[key] = value
    elif key.isdigit():
        my_dict[value] = int(key)
    inp_string = input()

for key, value in sorted(my_dict.items()):
    print(f"{key} -> {value}")
