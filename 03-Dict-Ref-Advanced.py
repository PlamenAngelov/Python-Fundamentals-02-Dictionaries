data = input()

dict_ref = {}

while data != "end":
    key = data.split(" -> ")[0]
    value = data.split(" -> ")[1]
    if value[0].isdigit():
        if key in dict_ref.keys():
            dict_ref[key] += ", " + (value)
        else:
            dict_ref[key] = value
    else:
        if value in dict_ref.keys():
            dict_ref[key] = dict_ref[value]
    data = input()


for key, value in dict_ref.items():
    print(f"{key} === {value}")