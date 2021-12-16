import random
text_file = open("password.txt", "r+")
linelist = text_file.readlines()
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
password = ""
length = int(input("How long do you want your password to be? "))
for i in range(length):
    password = password + random.choice(characters)
print(password)
print("Enjoy your password!")
input('Press ENTER to exit')
linelist.append(password)
for line in linelist:
    text_file.write(line+"\n")
text_file.close()
