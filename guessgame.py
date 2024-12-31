print("hello world")
import random
number_to_guess=random.randint(1,10)
print(number_to_guess)
attempt=0
print("+==============================+")
print("welcome to the number guessing game!!")
print("plese guess the nuber in specified range ") 
while True:
   guess=int(input("entr the guess: "))
   attempt+=1
   if guess>number_to_guess:
            
       print("too high")
   elif guess<number_to_guess:
         print("too  low")
   elif guess==number_to_guess:
         print(f"congratuation  you gete the number in attempt {attempt}")
         break
   else:
         print("ples guess in specified range")