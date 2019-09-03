import os
import random
guessnum = ()
mainnumber = random.randint(10,99)
print("Welcome to this game, In this game you need to guess the correct number.6\n Type 'start' when you want to start the 2 minutes")
start = input()
if start == "start":
    print("Off you go!")
    os.system("shutdown -s -t 120")
else:
    print("Please type 'start' to start")
print("Your number is inbetween 10 and 99 go!")
while guessnum != mainnumber:
    guessnum = int(input("Enter your guess: "))
os.system("shutdown -a")
print("Well done! the number you guessed correct was", mainnumber)
print("shutdown aborted!")

	
