input_key = input()
input_value = input()
n = int(input())

my_dictionary = {}
my_list = []

for i in range(0,n):
    input_text = input()
    my_list = list(map(str, input_text.split(" => ")))
    my_dictionary[my_list[0]] = list(map(str, my_list[1].split(";")))

for key, value in my_dictionary.items():
    if input_key in key :
        print(f"{key}:")
        for value in my_dictionary[key]:
            if input_value in value:
                print( f"-{value}")