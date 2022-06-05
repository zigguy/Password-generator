import pyperclip
import random
import array
text_file = open("password.txt", "a")
#linelist = text_file.readlines()
arr = []
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
special = "!@#$%^&*()"
password = ""
#everything below this are just choices for the characters above
while 1:
    lowercaseinput = input("Do you want lowercase letters in your password? (y/n): ")
    if (lowercaseinput == "y" or lowercaseinput == "n"):
        if (lowercaseinput == "y"):
            arr.append(lowercase)
        break
    if (lowercaseinput != "y" or lowercaseinput != "n"):
        print("Please enter y or n.")

while 1:
    uppercaseinput = input("Do you want uppercase letters in your password? (y/n): ")
    if (uppercaseinput == "y" or uppercaseinput == "n"):
        if (uppercaseinput == "y"):
            arr.append(uppercase)
        break
    if (uppercaseinput != "y" or uppercaseinput != "n"):
        print("Please enter y or n.")

while 1:
    numbersinput = input("Do you want numbers in your password? (y/n): ")
    if (numbersinput == "y" or numbersinput == "n"):
        if (numbersinput == "y"):
            arr.append(numbers)
        break
    if (numbersinput != "y" or numbersinput != "n"):
        print("Please enter y or n.")

while 1:
    specialinput = input("Do you want special characters in your password? (!@#$%^&*() (y/n): ")
    if (specialinput == "y" or specialinput == "n"):
        if (specialinput == "y"):
            arr.append(special)
        break
    if (specialinput != "y" or specialinput != "n"):
        print("Please enter y or n.")

    

length = int(input("How long do you want your password to be? "))
while (len(password) < length): #this makes the password
   for i in range(length):
      randomset = random.choice(arr)
      password = password + random.choice(randomset)
pyperclip.copy(password)
print(password)
print("Your password has been copied to your clipboard!")
print("Enjoy your password!")
input('Press ENTER to exit')
#linelist.append(password)
#for line in linelist:
text_file.write(password+' ')
text_file.write(name+"\n")
text_file.close()

#credits
#zigguy
#clairesaige for helping me making the password part and setting up the array properly
