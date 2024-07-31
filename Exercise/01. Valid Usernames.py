usernames = input().split(", ")

for username in usernames:
    if 3 <= len(username) <= 16:
        for char in username:
            if not any([char.isalnum(), char == "-", char == "_"]):
                break
        else:
            print(username)