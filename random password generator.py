import random
import string
characters=string.ascii_letters+string.digits+string.punctuation        #---Characters to be used in password generation

password=""

while True:
    choice=input("Enter 1 to generate password or 2 to exit: ")
    if choice=="1":
        length=int(input("Enter the length of password you want to generate: "))
        password=""
        for i in range(length):
            password+=random.choice(characters)
        print("Generated Password: ", password, " ", "(Length of password): ",len(password))        #---Output of generated password and its length
        print("---------------------------------------------------")
    elif choice=="2":       #---Exit the program
        break
    else:
        print("Invalid choice! Run the program again and please enter 1 or 2")      #---Error handling for invalid input
