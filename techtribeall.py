""" These is  a program that prompt the user to enter two number 
      and perform basic arthimetic opration 
      addition
      substraction
      multiplication
      division  
      and the like 

"""
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def product(x,y):
    return x*y
def division(x,y):
    if y!=0:
        return x/y
    else:
        return "ERROr division by zero does noe exist"
def find_power(x,n) :

    return pow(x,n)
def find(x):
    return x**2
print("=+++++++++++++++++++=")
print("select option ")
print("1,for add")
print("2,for substract")
print("3,for mltiply")
print("4,for division")
print("5,for power")
print("6,for square")
x=int(input("entr the  x:"))
y=int(input("entr the numberL y:"))
while True:
 
   choice=int(input("enter our chice:"))
   if choice==1:
     print(f"{x}+{y}={add(x,y)}")
   elif choice==2:
       print(f"{x}-{y}={substract(x,y)}")
   elif choice==3:
       print(f"{x}*{y}={product(x,y)}")
   elif choice==4:
       print(f"{x}-{y}={division(x,y)}")
   elif choice==5:
     n=int(input("enter the exponent:"))
       
     print(f"{x}the power of{n}={find_power(x,n)}")
   elif choice==6:
       print(f"{x}the power of 2={find(x)}")
   else:
       print("invalid input!!!")
       break
  
""" random number generator 
   in python 
"""

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
""" these is  aprogram that demonestrates 
dictionary in
 pyhton 
"""
my_description={"firstname":"Getabalew",
                "midlename":"Kemaw",
                "age":20,
                "lastname":"amare",
                "contact_us":{
                    "phonenumber":944463198,
                    "email":"getabalewkemaw@gmail.com"
                },
                "strit":"A.A_ataye main_road",
                "is_atudent":True,
                "city":"Debreberhan,Ethiopia",
                "campus_time":"secound year",
                "department":"software enginering",
                "skill":["HTML","css","javascript","python_beginner"],
                "sibling":("jhon"," aster","tesfa","helen"),
                "my_strength":["punctual"," professional",'ethical','hardworker'],
                "taken_course":{"python","discretemaths","database","fundamental of sw enginerring"}


}
# for keys,values in my_description.items():
#     print(f"{keys}:{values} ,end=" " ")
# print('Getabalew' in my_description)
# print(my_description.items())
for keys in my_description:
    if keys=="skill":
        for i in my_description["skill"]:
            print(i)
"""these is about sets  and
tuples 
in python


"""
# # set={"apple","banana","pineapple","cherry","mango"}
# print(set)
# set2={"apple","banana","cherry"}

# set2.add("mango")
# print(set2)

# set3={"pyhton","java","c++"}
# for list in set3:
#     print(list)
# animal={"dog","cat","rabbit"}
# animal.remove("dog")
# print(animal)
# print("cat" in animal)
# x={1,2,3}
# y={3,4,5,5,6}
# print(x.union(y)
# print(x.intersection(y))
# print(x.difference(y))
# print(x.symmetric_difference(y))
# my_list=[1,2,3,4,5,6,5,7,8,6]
# my_set=set()
# duplicate=set()
# for item in my_list:
#     if item in my_set:
#        duplicate.add(item)
#     else:
#         my_set.add(item)
# print(duplicate)
# print(my_set)
# my_tuple=("red","green","yellow","blue","purple","purple")
# print(my_tuple[1:4])
# print("grren" in my_tuple)
# for i in my_tuple:
#     print(i)
#     print(my_tuple.count("purple"))

# tuple=("apple",42,3.14,"banana")
# for i in tuple:
#     if type(tuple[i])==int and type(tuple[i])==float:
#         pass
# tuple=(1,2,3,4,5)
# length=0
# for i in tuple:
#     length+=1
# print(length)
# Combine the sets {1, 2, 3} and {3, 4, 5} using union().
# Find the intersection of {1, 2, 3, 4} and {3, 4, 5, 6}.
# Use the difference() method to find items in {1, 2, 3, 4} but not in {3, 4, 5, 6}.
# Create a set of numbers from 1 to 5 and remove all items using clear().
# Write a program to find duplicates in a list using a set.
# Hard Exercises
# Use a set to remove duplicate characters from a string.
# Input: "hello"
# Output: {'h', 'e', 'l', 'o'}
# Create two sets of student names and find the symmetric difference.
# Check if the set {1, 2} is a subset of {1, 2, 3}.
# Write a function that takes two sets and returns a new set with all unique elements from both sets.
# Create a program that counts the unique words in a sentence using a set.
# name="hello"
# my_set=set()

# for char in name:
#     my_set.add(char)
# print(my_set)
# st_name1={"getabalew","leta","samuel","gaddisa"}
# st_name2={"gaddisa","abebe","kebede"}
# print(st_name1.symmetric_difference(st_name2))
# set1={1,2}
# set2={1,2,3}
# print(set1.issuperset(set2))
# print(set1.issubset(set2))
"""" TECHTONIC TRIBE 
      TECH PROGRMAS OF PYHTON 
      UP TO KNOW 



"""