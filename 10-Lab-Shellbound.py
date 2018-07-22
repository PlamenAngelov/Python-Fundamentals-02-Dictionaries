import math
def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

inp_string = input()
shellbound_dict = {}

while inp_string != "Aggregate":
    inp_list = inp_string.split(" ")

    #if is_int_in_range(inp_list[1]):
    region = inp_list[0]
    shell_count = int(inp_list[1])

    if region in shellbound_dict.keys():
        check_list = shellbound_dict[region]
        if shell_count not in check_list:
            tmp_lst = shellbound_dict[region]
            tmp_lst.append(shell_count)
            shellbound_dict[region] = tmp_lst
    else:
        tmp_lst = []
        tmp_lst.append(shell_count)
        shellbound_dict[region] = tmp_lst

    inp_string = input()


for region, shell_count_lst in shellbound_dict.items():
    count_str = ", ".join(str(s) for s in shell_count_lst)
    giant_shell_size = sum(shell_count_lst) - (sum(shell_count_lst)/len(shell_count_lst))
    print(f"{region} -> {count_str} ({normal_round(giant_shell_size)})")