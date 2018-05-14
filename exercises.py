#Loops allows you to automatic repetitive tasks.
#You'll be practicing both for and while loops in this assignment.

#1. Uber This!
# Declare a variable named cars and assign it a list of 5 of your favorite car brands. Next create a for loop that will iterate through the cars list and prints the following: 'My next car will be a red x.' Where x represents each item in the list.

cars = ['Toyota', 'Tesla', 'BMW', 'Porche', 'Mercedes'] 
for car in cars:
    print('My next car will be a red ' + car + '.')
    
#2  No More Tears
# Create a for loop that will iterate through the cyber attacks list and prints the following: 
#The attack at 0 is Wannacry.
#The attack at 1 is Petya.
#The attack at 2 is Locky.
#The attack at 3 is Krack Attack
#The attack at 4 is Sambacry.
#DO NOT use numbers in your string.

cyber_attacks = ['Wannacry', 'Petya', 'Locky', 'Krack Attack', 'Sambacry']
for attack in cyber_attacks:
     print('The attack at ' + str(cyber_attacks.index(attack)) + ' is ' + attack + '.')

#3 Even
# Declare a variable named even_list and assign it an empty list. Next write a for loop that will place 25 even numbers starting from 0 into the even_list list. Print the even_list variable to see your results. 

even_list = []
num_list = range(0, 51)
# print(num_list)
for number in num_list:
    if(number%2 == 0):
        even_list.append(number)
print(even_list)

#4 Sum Up
# Create a function named add_up which takes a parameter num. In the code block inside the function, create a variable named sum and assign it a number value of 0. Next create a for loop that will iterate through a list of numbers using the range function that will be determined by the num parameter and will sum up all the numbers in the list and store it to the sum variable. Print the sum variable to see your results.

#i.e a number list of 10 will have a sum total of 45
def add_up(num):
    sum = 0
    for number in range(num):
        sum += number
    print sum
add_up(10)



