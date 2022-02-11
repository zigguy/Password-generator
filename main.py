import random
import array
text_file = open("password.txt", "w+")
linelist = text_file.readlines()
arr = []
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
special = "!@#$%^&*()"
password = ""
#everything below this are just choices for the characters above
lowercaseinput = input("Do you want lowercase letters in your password? (y/n): ")
if (lowercaseinput == "y"):
    arr.append(lowercase)
uppercaseinput = input("Do you want uppercase letters in your password? (y/n): ")
if (uppercaseinput == "y"):
    arr.append(uppercase)
numbersinput = input("Do you want numbers in your password? (y/n): ")
if (numbersinput == "y"):
    arr.append(numbers)
specialinput = input("Do you want special characters in your password? (!@#$%^&*() (y/n): ")
if (specialinput == "y"):
    arr.append(special)
length = int(input("How long do you want your password to be? "))
while (len(password) < length): #this makes the password
   for i in range(length):
      randomset = random.choice(arr)
      password = password + random.choice(randomset)
print(password)
print("Enjoy your password!")
input('Press ENTER to exit')
linelist.append(password)
for line in linelist:
    text_file.write(line+"\n")
text_file.close()
#credits
#zigguy
#clairesaige for helping me making the password part and setting up the array properly