#Guess the Number "Too High or Too LoW" Using While Loop
import random #import the random directory
myName = input("Enter your name: ")
print ("Hey! ", myName, "I am thinking of a number between 10 - 15, can you guess what that is? ")

number = random.randint(10,15)#Random numerbetween 10-15
guess = int(input("What is your guess?")) #using guess as variable
gcount=0;
while gcount<=4:# counting the guess
  print("you are on guess",gcount)
  guess = int(input("What is your guess?")) 
  gcount=gcount+1

  if (guess==number):
     print("Well done ",myName, "you gussed my number ")
     break
  elif guess<number:#when guess is less than the number
     print("you are too low")
     
  else:#when guess is more than the number
    print("you are too high")  

print("thanks for playing")