def Exercise_1():
    names = ["john smith", "jay santi", "eva kuki"]
    new_names=[item.title() for item in names]
    print(new_names)

def Exercise_2():
    usernames = ["john 1990", "alberta1970", "magnola2000"]
    new_usernames=[len(item) for item in usernames]
    print(new_usernames)


def Exercise_3():
    user_entries = ['10', '19.1', '20']
    new_user_entries= [float(item) for item in user_entries]
    print(new_user_entries)

def Exercise_4():
    user_entries = ['10', '19.1', '20']
    new_user_entries = [float(item) for item in user_entries]
    print(sum(new_user_entries))

Exercise_4()