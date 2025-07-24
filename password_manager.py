master_password = input("What is the master password?: ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print(f"Username: {user} , Password: {password}")

def add():
    username = input("Enter the username: ")
    passw = input("Enter the password for this user: ")

    with open("passwords.txt", "a") as f:
        f.write(username +  "|" + passw + "\n")

while True:
    mode = input("Would you like to view or add a password(view/add), type q to exit?: ")

    if mode == "view":
        view()
    elif mode =="add":
        add()
    elif mode == "q":
        break