input_string = input()

my_dictionary ={}

for i in range(0, len(input_string)):
    if input_string[i] in my_dictionary.keys():
        my_dictionary[input_string[i]] += 1
    else:
        my_dictionary[input_string[i]] = 1

for item,value in my_dictionary.items():
    print(f"{item} -> {value}")

