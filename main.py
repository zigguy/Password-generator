import random
text_file = open("password.txt", "w+")
linelist = []
for line in text_file.readlines():
    if line != "\n":
        linelist.append(line)
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

while True:
    password = ""
    length = int(input("How long do you want your password to be? "))
    for i in range(length):
        password = password + random.choice(characters)
    print(password)
    print("Enjoy your password!")
    log = input("Do you want to log this password? (y/n): ")
    if log == "y":
        linelist.append(password)
    while log != "y" and log != "n":
        print("Please enter y or n.")
        log = input("Do you want to log this password? (y/n): ")
        if log == "y":
            linelist.append(password)    
    play_again = input("Want to create another password? (y/n): ")
    if play_again.lower() == "n":
        text_file.close()
        break
    while play_again.lower() != "y" and play_again.lower() != "n":
        print("Please enter y or n.")
        play_again = input("Want to create another password? (y/n): ")
        if play_again.lower() == "n":
            text_file.close()
            break

updated_file = open("password.txt", "w")
for line in linelist:
    line = line.strip()
    updated_file.write(line+"\n")
updated_file.close()
