str_input = input()
city_dict = {}

while str_input != "ready":
    split_list = []
    temp_list = []
    split_list = str_input.split(":")
    temp_list = split_list[1].split(",")

    if split_list[0] in city_dict.keys():
        tmp_lst = city_dict[split_list[0]]
        for item in temp_list:
            city_dict[split_list[0]].append(item)
    else:
        city_dict[split_list[0]] = temp_list

    str_input = input()

my_dict = {}
for key, value in city_dict.items():
    temp_dict ={}
    for item in value:
        veh_count_list = item.split("-")
        temp_dict[veh_count_list[0]] = int(veh_count_list[1])
    my_dict[key] = temp_dict

str_input = input()
check_dict = {}
while str_input != "travel time!":
    city_people_list = list(map(str, str_input.split(" ")))
    check_dict[city_people_list[0]] = int(city_people_list[1])
    str_input = input()

for city, peopleCount in check_dict.items():
    if city in my_dict.keys():
        transportCapacities = sum(my_dict[city].values())
        if peopleCount <= transportCapacities:
            print(f"{city} -> all {peopleCount} accommodated")
        else:
            print(f"{city} -> all except {peopleCount - transportCapacities} accommodated")
