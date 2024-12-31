
# def find_sum(x,y):
#     return x+y
# print(find_sum(12,13))
# def find_area(radius):
#     return 3.14 *radius*radius
# print(find_area(10))


# def add_all_num(*nums):

#     total=0
#     for i in nums:
#         total+=i
#     return total
# print(add_all_num(1,2,3,4,5,6))

# def tem_converter_fht(cel):
#    f=(cel*9/5)+32
#     rerurn f
# print(tem_converter_fht(39))

# def c(t):
#     f=(t*9/5)+32
#     return f
# print(c(45))

# # Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# # Write a function called calculate_slope which return the slope of a linear equation
# # Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# # Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# def check_season(month):
   
    

    
#     if month in ['december', 'january', 'february']:
#         return "Winter"
#     elif month in ['march', 'april', 'may']:
#         return "Spring"
#     elif month in ['june', 'july', 'august']:
#         return "Summer"
#     elif month in ['september', 'october', 'november']:
#         return "Autumn"
#     else:
#         return "Invalid month"


# month = "march"
# season = check_season(month)
# print(f"The season in {month} is {season}.")


# def calculate_slope(x1, y1, x2, y2):
    
#     if x1 == x2:
#         return "Slope is undefined (vertical line)"
    
#     # Calculate the slope
#     slope = (y2 - y1) / (x2 - x1)
#     return slope

# # Example usage
# x1, y1 = 1, 2
# x2, y2 = 3, 4
# slope = calculate_slope(x1, y1, x2, y2)
# print(f"The sl"ope of the line is {slope}"")

"""these is  aprogram 
the finds root 


"""
# def finds_quadratic(a,b,c):
#     # qua=a*x*x+b*x+c
#     x=-b +pow((b*b-4*a*c),0.5)/2*a
#     d=b*b-4*a*c
#     if d==0:
     
#       print("one solution ")
#       print(x)
#     elif d>0:
#         print("two solution in equation")
#         x=-b +pow((b*b-4*a*c),0.5)/2*a
#         y= -b-pow((b*b-4*a*c),0.5)/2*a
#         print(int(x))
#         print(int(y))
#     elif d<0:
#         print("no solution ")
      
#     else:
#         print("invalid input")

# finds_quadratic(1,-3,2)



# def print_list(*nums):
#     m=[]
#     for x in nums:
#         m.append(x)
#     return m
# print(print_list(1,3,5,7,8,765))




# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

# def reverse_list(array):
#     reversed_array = []
#     for i in range(len(array) - 1, -1, -1):  # Loop from the last index to the first
#         reversed_array.append(array[i])
#     return reversed_array

# # Test cases
# print(reverse_list([1, 2, 3, 4, 5]))
# # Output: [5, 4, 3, 2, 1]

# print(reverse_list(["A", "B", "C"]))
# # Output: ["C", "B", "A"]




# capitalize the first items 
# def my_capitalized(list):
#     lst=[]
#     for i in list:
#         lst.append(i.capitalize())
#     return lst
# print(my_capitalized(["getabalew","leta"]))


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

# def food_stuf(my_list,item):
#     my_list.remove(item)
#     return my_list
# # food=["bava","mango","tea"],
# print( food_stuf(["bava","mango","tea"],"tea"))



# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
# Write a functions which checks if all items are unique in the list.
# Write a function which checks if all the items of the list are of the same data type.
# Write a function which check if provided variable is a valid python variable
# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.


# import statistics
# def calmean(data):
#     if len(data)==0:
#         return None
#     return sum(data)/len(data)
# def calcmedian(data):
#     if len(data)==0:
#         return None
#     return statistics.median(data)
# def calcmode(data):
#     if len(data)==0:
#         return None
#     return statistics.mode(data)
# def calcvar(data):
#     if len(data)<2:
#         return None
#     return statistics.variance(data)
# def calcstdv(data):
#     if len(data)<2:
#         return None
#     return statistics.stdev(data)
# def calcerange(data):
#     if len(data)==0:
#         return None
#     return max(data)-min(data)
# list1=[1,2,3,4,5,6,6,7,7,8,7]
# print(calmean(list1))
# print(calcmedian(list1))
# print( calcmode(list1))
# print(calcerange(list1))
# print(calcvar(list1))
# print(calcstdv(list1))

# Write a function called is_prime, which checks if a number is prime.


def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    divisor_count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisor_count += 1
    return divisor_count == 2  # A prime number has exactly two divisors: 1 and itsel
print(is_prime(17))
print(is_prime(9))

countries = [
    {"country": "China", "languages": ["Mandarin"]},
    {"country": "India", "languages": ["Hindi", "English"]},
    {"country": "United States", "languages": ["English"]},
    {"country": "Indonesia", "languages": ["Indonesian"]},
    # Add more countries and languages...
]
from collections import Counter

# Function to get the most spoken languages in the world
def most_spoken_languages():
    from countries_data import countries  # Assuming countries_data.py contains the necessary data

    language_counter = Counter()

    # Count occurrences of each language
    for country in countries:
        for language in country['languages']:
            language_counter[language] += 1
    
    # Get the 10 most common languages (you can change the number to 20 for top 20)
    most_common_languages = language_counter.most_common(10)

    return most_common_languages

























