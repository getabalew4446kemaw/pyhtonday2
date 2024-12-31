# class car:
#     def __init__(self,name,type,regnumber,speed,color,wheller,length):
#         self.name=name
#         self.type=type
#         self.regnumber=regnumber
#         self.speed=speed
#         self.color=color
#         self.wheller=wheller
#         self.legth=length
#     def drive(self):
#         print("the car is driving ")
#     def spd(self):
#         print("yh thecar is moving with a peed of 10 km pe hour ")
#     def for_sale(self):
#         print(f"the car is,{self.name } for sale if any one want it can buy with appropirate price")

# p1=car("picap","speedy",132345,30,"redyblue","4  wheller","16 metre")
# p2=car("picap","speedy",132345,30,"redyblue","4  wheller","16 metre")
# print(p1.color)
# print(p1.regnumber)
# print(p1.wheller)
# print(p1.name)
# print(p1.type)
# # print(car.drive())
# # print(car.spd())
# p2.drive()
# p2.spd()
# p1.for_sale()





# class  Student:
#     class_year=2024
#     num_students=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         Student.num_students+=1
# stud1=Student("GETABALEW",20)
# stud2=Student("SAMUEL",21)
# stud3=Student("leta",22)
# print(stud1.name)
# print(stud1.age)
# print(stud1.class_year)

# print(stud2.name)
# print(stud2.age)
# print(stud2.class_year)
# print(Student.num_students)
# print(f"my name is {stud1.name} i am graduating in the year{Student.class_year} FROM THE NUMBER OF STUDENTS{Student.num_students}")




# # INHERITANCE IN PYHON
# class animal:
#     def __init__(self,name):
#         self.name=name
#         self.is_active=True
#         def eat(self):
#              print(f"{self.name} is eating now ")
#         def sleep(self):
#              print(f"{self.name} is curently slleping")
# class dog(animal):
#         def speak(self):
#               print("woof")
#         def eat(self):
#              print(f"{self.name} is eating now ")
#         def sleep(self):
#              print(f"{self.name} is curently slleping")
# class cat(animal):
#         def speak(self):
#               print("meow")
#         def eat(self):
#              print(f"{self.name} is eating now ")
#         def sleep(self):
#              print(f"{self.name} is curently slleping ")
        
# class moouse(animal):
#         def eat(self):
#              print(f"{self.name} is eating now ")
#         def sleep(self):
#              print(f"{self.name} is curently slleping")
# dog1=dog("scrooby")
# cat1=cat("smiled cat")
# moouse1=moouse("my keyboard mouse")
# print(cat1.name)
# cat1.eat()
# cat1.sleep()
# print(cat1.is_active)
# cat1.speak()




# #multiple inheritance
# class animal:
#     def __init__(self,name):
#          self.name=name
         
#     def eat(self):
#             print(f"this animal {self.name}is eating")
#     def sleep(self):
#       print(f"this animal{self.name} is sleeping")
# class prey(animal):
#     def flee(self):
#          print(f"the aniaml {self.name}is fleeing")
# class predator(animal):
#      def hunt(self):
#           print(f"the animal{self.name} is hunting")
# class rabbit(prey):
#      pass
# class hawk(predator):
#      pass
# class fish(prey,predator):
#      pass


# rab=rabbit("lebewa")
# rab.flee()
# rab.eat()
# # rab.hunt()
# fi=fish("arifu asa")
# fi.hunt()
# fi.flee()
# fi.sleep()
# fi.eat()
# hw=hawk("tire leba")
# hw.hunt()
# fish inherit from all the  class
#ranbbit inherit from prey and animal only 
#hawk inherit frm predator and animal  only 
# this scenario is called multple inheritance


# class Library:
#     def __init__(self,libraryname,postion,listofbooks):
#         self.libraryname=libraryname
#         self.postion=postion
#         self.listofbooks=listofbooks

# lib_description=Library("TESFA GEBRE SELASE","IN FRONT OF MAIN CAFFE",["FRESH MANB OOKKS","ENGINNERING GUIDE ","D/T MATERIAL"])
# print(lib_description.libraryname)
# print(lib_description.listofbooks)
# print(lib_description.postion)

# class Student:
#     def __init__(self,name ,age,grades,course):
#         self.name=name
#         self.age=age
#         self.grades=grades
#         self.course=course
     

# student_description=Student("Getabalew",20,{"maths":"A+",
#                                             "C++":"A",
#                                              "geo":"A+",
#                                              "English":"A"},
#                                              ["MATHS","ENGLISH","C++"]
#                                              )
# print(student_description.name)
# print(student_description.age)
# print(student_description.grades)
# print(student_description.course)

# class School:
#    def __init__(self,schname,numofstudent,studnamewithgrade):
#         self.schname=schname
#         self.numofstudent=numofstudent
#         self.studnamewithgrade=studnamewithgrade
#    def descript(self):
#        print("+++++++++++++++++++++++++++++")
#        print("welcome to the universty description ")
# description=School("Debreberhan university",5,{"getabalew":4.00,
#                                                "samuel":4.00,
#                                                "leta":4.00,
#                                                "kura":4.00,
#                                                "samre":3.98}
#                                                )
# description.descript()
# print(description.schname)
# print(description.numofstudent)
# print(description.studnamewithgrade)
# class Animal:
#     def __init__(self,name ,species):
#         self.name=name
#         self.species=species
#     def describe(self):
#       return f"name:{self.name} species:{self.species}"
#     @classmethod
    
#     def describeinfo(cls):
#       return f"this is the {cls.species} representing animal"
#     @staticmethod
#     def is_domestic(species):
#         domestic_species=["dog","cat","ox","rabbit"]
#         if species.lower() in domestic_species:
#            return True
#         else:
#            return False
# animal1=Animal("CHARLIE","DOG")
# print(animal1.describe)
# print(Animal.describeinfo)
# print(Animal.is_domestic("CAT"))
# print(Animal.is_domestic("LION"))


# class Animal:
#     # Constructor to initialize the name and species of the animal
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     # Instance method to describe the animal (name and species)
#     def describe(self):
#         return f"Name: {self.name}, Species: {self.species}"

#     # Class method to display class-level information
#     @classmethod
#     def display_class_info(cls):
#         return f"This is the {cls.__name__} class, representing animals."

#     # Static method to check if the species is domestic or wild
#     @staticmethod
#     def is_domestic(species):
#         domestic_species = ["dog", "cat", "rabbit", "guinea pig"]
#         if species.lower() in domestic_species:
#             return True
#         return False


# # Example Usage:

# # Creating an instance of the Animal class
# animal1 = Animal("Charlie", "dog")

# # Calling the instance method describe
# print(animal1.describe())  # Output: Name: Charlie, Species: dog

# # Calling the class method display_class_info
# print(Animal.display_class_info())  # Output: This is the Animal class, representing animals.

# # Calling the static method is_domestic
# print(Animal.is_domestic("dog"))  # Output: True
# print(Animal.is_domestic("lion"))  # Output: False


# class Employee:
#     def __init__(self,name,position):
#         self.name=name
#         self.position=position
#     def describe_info(self):
#         return f"{self.name}={self.position}"
#     @staticmethod
#     #uses when you want to set condition  and it is used in class name not obbect name
#     def is_valid_postion(postion):
#         valid_position=["eniginner","manager","secretary"]
#         return postion.lower() in valid_position
# emp1=Employee('getabalew',"secretary")
# emp2=Employee("SAMUEL","MANAGER")
# emp3=Employee("leta","radiologist")
# print(emp1.describe_info())
# print(emp2.describe_info())
# print(emp3.describe_info())

# print(Employee.is_valid_postion("FABRICIST"))
# print(Employee.is_valid_postion("manager"))


class Student:
    count =0
    totals=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
        Student.totals+=gpa
    def describe(self):
        return f"{self.name}:{self.gpa}"
    @classmethod
    def get_count(cls):
        return f"the count is{cls.count}.count"
    @classmethod
    def get_average(cls):
         if cls.count==0:
             return 0
         else:
             return f"the average is {cls.totals/cls.count}"
stud1=Student("getabalew",4.00)
stud4=Student("getbalew",4.00)
stud3=Student("getabalew",4.00)
stud2=Student("getablew",4.00)
print(stud1.describe())
print(stud2.describe())
print(stud3.describe())
print(stud4.describe())
print(Student.get_count())
print(Student.get_average())
"""" these code is all about class 
 ddddddddddddddkGYYYXIKSO



"""
