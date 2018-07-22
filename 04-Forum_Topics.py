data = input()

dict = {}

while data != "filter":
    topic = data.split(" -> ")[0]
    tags = data.split(" -> ")[1]

    if topic not in dict.keys():
        temp_list = tags.split(", ")
        dict[topic] = temp_list
    else:
        tags = tags.split(", ")
        for item in tags:
            temp_list = dict[topic]
            if item not in temp_list:
                dict[topic].append(item)

    data = input()

data = input()
search_tags = data.split(", ")
new_dict = {}

for topic, tags in dict.items():
    count = 0
    for i in range(0, len(search_tags)):
        if search_tags[i] in tags:
            count += 1
    if count == len(search_tags):
        for j in range(0, len(tags)):
            tags[j] = "#" + tags[j]
        new_dict[topic] = tags

for topic, tags in new_dict.items():
    print(f"{topic} | " + ", ".join(tags))