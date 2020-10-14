def mk_passwd(name):
    import random
    while True:
        if " " in name:
            name = input("There must be no space in your input. Please try again: ")
        else:
            break
    newname = list(set(name.lower()))
    passwd = "".join(random.choices(newname, k = 3)) + str(random.randrange(1000, 9999))
    return str(passwd)
        
name = input("Please enter your full name (without any spaces): ")
print(mk_passwd(name))