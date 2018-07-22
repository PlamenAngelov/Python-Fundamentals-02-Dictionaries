cloths = []
dict_cloths = {}

number = int(input())

for i in range(0, number):
    value = input()
    cloths.append(value)

look = input().split(' ')
color1 = look[0]  # Because the variable color is used several times later - change here to color1
dress = look[1]

for j in cloths:
    j = j.split(' -> ')
    dict_cloths.setdefault(j[0], []).append(j[1].split(','))

# New code to replace the old one

# Replace the list of lists in the cloths values for each color key
for color in dict_cloths:
    dict_cloths[color] = [item for sublist in dict_cloths[color] for item in sublist]

# Create dict for unique cloths with value their count
for color in dict_cloths:
    temp_list_clothes = dict.fromkeys(dict_cloths[color]).keys()
    temp_list_clothes_num = [dict_cloths[color].count(el) for el in temp_list_clothes]
    dict_cloths[color] = dict(zip(temp_list_clothes, temp_list_clothes_num))

# Print
for k in dict_cloths:
    print(f'{k} clothes:')
    temp_dict = dict_cloths[k]
    for cloth in temp_dict:
        found_word = ''
        if k == color1 and cloth == dress:
            found_word = ' (found!)'
        print(f'* {cloth} - {temp_dict[cloth]}{found_word}')