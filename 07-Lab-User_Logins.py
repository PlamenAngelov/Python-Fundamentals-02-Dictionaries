inp_string = input()
credentials_dict = {}

while inp_string != "login":
    temp_list = []
    temp_list = inp_string.split(" -> ")
    username = temp_list[0]
    password = temp_list[1]
    credentials_dict[username] = password
    inp_string = input()



inp_string = input()
login_failed_count = 0

while inp_string != "end":
    temp_list = []
    temp_list = inp_string.split(" -> ")
    username = temp_list[0]
    password = temp_list[1]

    if username in credentials_dict:
        if credentials_dict[username] == password:
            print(f"{username}: logged in successfully")
        else:
            print(f"{username}: login failed")
            login_failed_count += 1
    else:
        print(f"{username}: login failed")
        login_failed_count += 1
    inp_string = input()


if login_failed_count > 0:
    print(f"unsuccessful login attempts: {login_failed_count}")