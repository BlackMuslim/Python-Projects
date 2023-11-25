
print("Welcome to the NBA""\" Top Five \"Ranking System!")
print("Please Enter Your First Name: ")

name = input()

print( name + " Please Rank The Following Top 5 Players from Worst to Greatest, With The Greatest Being Ranked Number 1")

player = ["Luka","Zion","Shaq", "Kyrie", "Lamelo"]

print("*")
print("Luka")
print("Zion")
print("Shaq")
print("Kyrie")
print("Lamelo")
print("*")


while True: 
    number1 = input("Please Enter Your First Choice: ")

    if number1.lower() == "luka" or number1.lower() == "zion" or number1.lower() == "shaq" or number1.lower() == "kyrie" or number1.lower() == "lamelo":
        print("Thank you for your response!")
        break
    else:
        
        print("Please Enter One Of The Five Listed Players")
        

while True:
    number2 = input("Please Enter Your Second Choice: ")

    if number2.lower() == "luka" or number2.lower() == "zion" or number2.lower() == "shaq" or number2.lower() == "kyrie" or number2.lower() == "lamelo":
        print("Thank you for your response!")
        break
    else:

        print("Please Enter One Of The Five Listed Players")
        

while True:
    number3 = input("Please Enter Your Third Choice: ")

    if number3.lower() == "luka" or number3.lower() == "zion" or number3.lower() == "shaq" or number3.lower() == "kyrie" or number3.lower() == "lamelo":
        print("Thank you for your response!")
        break
    
    else:
        print("Please Enter One Of The Five Listed Players")
        

while True:
    number4 = input("Please Enter Your Fourth Choice: ")

    if number4.lower() == "luka" or number4.lower() == "zion" or number4.lower() == "shaq" or number4.lower() == "kyrie" or number4.lower() == "lamelo":
        print("Thank you for your response!")
        break
    
    else:
        print("Please Enter One Of The Five Listed Players")
        

while True:
    number5 = input("Please Enter Your Fifth Choice: ")

    if number5.lower() == "luka" or number5.lower() == "zion" or number5.lower() == "shaq" or number5.lower() == "kyrie" or number5.lower() == "lamelo":
        print("Thank you for your response!")
        break
    
    else:
        print("Please Enter One Of The Five Listed Players")
        


print("Your selections have been completed!")

print("In your opinion, the TOP 5 ranking are as follows: ")

print( "1st: " + number1)
print( "2nd: " + number2)
print( "3rd: " + number3)
print( "4th: " + number4)
print( "5th: " + number5)

print(" Thanks for playing " + name + "!")
