# Exercise 1
# Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]
# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]
l_2 =[]

def new_list():
    for i in range(len(l_1)):
        if l_1[i] <= 10:
            l_2.append(l_1[i])
    print(l_2)

new_list()


# Exercise 2
# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

list_1 = [1,2,3,4,5,6]
list_2 = [3,4,5,6,7,8,10]

def list_3():
    list_3 = sorted(list_1 + list_2)
    print(list_3)
list_3()