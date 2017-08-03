#Satire take on the classic Guess the Number, now you take a number, I guess it for you!

import random

print("Hi, What is your name?")
your_name = input()

print(your_name + ', think of a number from 1 to 10')
print("Done? Let me think...")


guess = random.randint(1,10)
print("Is your number {}?".format(guess))
print("Type Y if it really is your number, else say N")

your_response=input("Enter response here:")

if your_response == "Y":
    print("AWESOME!!! I got your number on the 1st try. 1/10 probability")

    
elif your_response == "N":
     while True:
        print("Type 'G' if your number is greater or 'L' if your number is lesser than my guess")
        your_response_again = input("Enter response here:")   
    
        if your_response_again == "G":
            guess = random.randint(guess,10)
        
        elif your_response_again == "L":
            guess = random.randint(0,guess)
        
        else:
            print("Wrong response")
            break
                
        
        print("Is your number {}?".format(guess))
        print("Type Y if it really is your number, else say N")
        your_response_once_again = input("Enter response here:")

        if your_response_once_again == "Y":
            print('Awesome,see ' + your_name + '! I guessed your number finally, although it depends on how much honest you are being with me :-P')
            break
        
        
                
else:
    print("Wrong response")
    

