inp_string = input()
position_dict = {}
salary_dict = {}
age_dict = {}

def is_float(value):
  try:
    num = float(value)
  except ValueError:
    return False
  return True

def is_int(value):
  try:
    num = int(value)
  except ValueError:
    return False
  return True

while inp_string != "filter base":
    temp_list = []
    temp_list = inp_string.split(" -> ")
    name = temp_list[0]
    value = temp_list[1]
    if is_int(value):
        age_dict[name] = int(value)
    elif is_float(value):
        temp1=[]
        temp1 = value.split(".")
        if int(temp1[1]) == 0:
            age_dict[name] = int(temp1[0])
        else:
            salary_dict[name] = float(value)
    else:
        position_dict[name] = value

    inp_string = input()


filter_by = input()

if filter_by == "Position":
    for name, value in position_dict.items():
        print(f"Name: {name}")
        print(f"{filter_by}: {value}")
        print("="*20)
elif filter_by == "Salary":
    for name, value in salary_dict.items():
        print(f"Name: {name}")
        print(f"{filter_by}: {value}")
        print("=" * 20)
elif filter_by == "Age":
    for name, value in age_dict.items():
        print(f"Name: {name}")
        print(f"{filter_by}: {value}")
        print("=" * 20)

