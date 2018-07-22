data = input()
city_capacity_dict = {}


while data != "ready":
    city = data.split(":")[0]
    list_transport = data.split(":")[1].split(",")

    if city not in city_capacity_dict:
        city_capacity_dict[city] = {}

    for item in list_transport:
        transport = item.split("-")[0]
        capacity = item.split("-")[1]


        city_capacity_dict[city][transport] = int(capacity)

    data = input()

data = input()

while data != "travel time!":
    city = data.split(" ")[0]
    people = int(data.split(" ")[1])

    count = 0
    for item in city_capacity_dict[city]:
        count += city_capacity_dict[city][item]

    if count >=  people:
        print(f"{city} -> all {people} accommodated")
    else:
        print(f"{city} -> all except {people - count} accommodated")

    data = input()