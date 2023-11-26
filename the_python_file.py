#This is a comment 

#It doesn't 
# matter how many lines


print("hello_kekambas!") # This is a comment after code that executes!

#variable defenition 
#syntax --> <variable> = <value>
x = 5 
some_group_of_chars = 'string'

# Data types
    # Numbers
        #Integer, float, (and complex)
    # string 
    # list, range, 
    # (dictionary)
    # bool
    # Nonetype    

# nums
# integer --> pretty much a whole number
num1 = 10 
num2 = -33
num3 = 30
num4 = float(num1)
print(type(num1))
print(type(num4))
#floats  they have a decimal
num5 = 5.0
print(type(num5))

# math operators

print("\n MATH OPERATORS:")

#add +
print(num1 + num3)

# subtract
print(num3 - num1)
print(30 - 10)

# multiply *
print(num1 * num3)

# divide / Always results in a float!
print(type(num3 / num1))

# floor division //  Always results in an interger (whole number)
print(27//5)
print(25//5)

# modulo %  Always results in an integer 
print(27 % 5)
print(25 % 5)

#side-bar: = vs ==
# = this is assigning a value (MAKE this equal to)
# == this is checking for equality (IS this equal to???) checking for type AND value equality
# will always result in a boolean
# ALSO comaprison operators:
# ==  equal
# !=  NOT equal 
# <     less than 
# >     greater than
# <=  less than OR equal to 
# >=  greater than OR equal to 

#THIS is an importnat one! %
# even or odd?
print(26 % 2 == 0)
print(27 % 2 != 0)

print(27 % 2 == 1)


#exponenets ** To the power of 
print(5 ** 5)


#side-bar variable naming conventions:
#int("33")
#int = 56
#int("987435") 
# Dont use pre-defined character sets 

# strings
# indexed, iterable, immutable
# It's a bunch of charachters inside of quotes . . .
st1 = 'this is a string'
st2 = 'this too!'
st3 = "So's this"
# double or single quotes are fine. just make sure that the other kind surrounds their use inside OR use an escape charachter
st4 = 'so\'s this'

print(type(st1))

print(st1[2]) # Indexed
print('string'[0])

# concatenation  a fancy way of saying adding strings together
print(st1 + '.' + st2)

# Interpolation  an even fancier way to day we're gonna add strings and pythin thingd together
# f - string
f_string = f"This is an f-string that also has this from python -->{num2 + 100}"
print(f_string)
f_name = 'steve'
print(f"Hello {f_name.title()}!")

print('arnold'.title())
# print(num3.title())

print(f_name.upper())
print(f_name.lower())

# methods vs fucntions
# methods and fucntions are the same thing . . . EXCEPT methods work on a specific data type
# they syntax is what gives it away! <data_type>.method(paramerter) vs function(parameter)


print('\nLISTS:')
# lists 
# also called array
# ordered/indexed, iterable, and muteable
# syntax <variablename> = []
# contains valubales seperated by commas
# can store just about anything in a list 
my_list = []
my_list2 = [1, 2, 3, 4, 5]
my_list3 = ['1', '2', '3', '4', '5']
confused = [1, '2', 'three', 4.0, True, None]

print(my_list2[3])
print(my_list2)

print(confused[-2])

# .append() - adds am item to the end of the list
my_list.append('Steve')
my_list.append('Arnold')
print(my_list)
my_list.append('Valarie')
my_list.append('Jill')
print(my_list)
my_list.append('Javan')
print(my_list.append('Santeri'))
print(my_list)

# list.pop() - removed the last item from the list 
# BUT you can save the value from .pop() aka it returns the value
# AND there's an optional parameter that you can specify the index


popped = my_list.pop(2)
print(my_list)
print(popped)

r_exp = [1, 1, 1, 23, 45, 56]
# list.remove() - removes a value from the list, but note it is the firs occurance!
# list.remove(value)
r_exp.remove(1)
r_exp.remove(1)
r_exp.remove(1)
print(r_exp)


print(my_list)
my_list.append("Jill")

my_list.remove("Jill")
print(my_list)

# membership check --> the word 
# in 
print('Jill' in my_list)
print("Joe" in my_list)
print('n' in "None")

# conditional! if, elif, else
# we can use as many if statments as we want, each one checks for a circumstance to be true
# if we want to check the same variable against other circumstances we would use elif, or else
# we WILL always have an if, we CAN have as many elids after that as we want, and we CAN fish after that with an else

print('\n AGE and conditionals')
age = 54

if age > 64:
    print('senior')
elif age > 17:
    print("Adult")
else: 
    print('kid')

if age > 17 and age < 65: 
    print('target audience')
else:
    print('not our audience')

#truth tree

# T and T == T
# T and F == F
# F and F == F

# T or T == T
# T or F == T
# F or F == F 


# Functions 
# syntax def func(parameter):
#                   codeblock to execute
# def function_name(parameter1, parameter2. . .)
#                  codeblock

def odd(num):
    if num % 2 == 0:
        print('EVEN')
    else:
        print("ODD")

odd(4)

print("\n retun vs. print example")

def add(a, b):
    print(a + b)

def mult(a, b):
    return a * b

add(5, 5)
print(mult(5, 5))
add(mult(5, 5), 25)     
# mult(add(5, 5), 10)
print(mult(5, 5)== 25)
print(add(5, 5)== 25)
print(add(345, 345) ==None)

this_str = input('what\'s your name?\t')
print(this_str)
print(type(this_str))
print(this_str.upper())