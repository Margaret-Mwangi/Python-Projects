from cryptography.fernet import Fernet

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key() """

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
        return key


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("Username:" ,user, "Password:" ,fer.decrypt(password.encode()).decode())

def add():
    username = input("Enter the username: ")
    passw = input("Enter the password for this user: ")

    with open("passwords.txt", "a") as f:
        f.write(username +  "|" + fer.encrypt(passw.encode()).decode() + "\n")

while True:
    mode = input("Would you like to view or add a password(view/add), type q to exit?: ")

    if mode == "view":
        view()
    elif mode =="add":
        add()
    elif mode == "q":
        break