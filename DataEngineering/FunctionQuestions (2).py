#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:


def int_divis(input_int):
    global divisor_list
    divisor_list=[]
    for i in range(1,input_int+1):
        if input_int%i == 0:
            divisor_list.append(i)
    
    return divisor_list
int_divis(12)


# In[3]:


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def factor_check(integer_1,integer_2):
    int_divis(max(integer_1,integer_2))
    if min(integer_1,integer_2) in divisor_list:
        print("True")
    else:
        print("false")
    
factor_check(42,168)


# In[4]:



# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet


# A2a:
def alpha_loc(input_string):
    global location
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    location = alphabet.find(input_string)
    return location

    

alpha_loc("j")




# In[5]:


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def name_id(input_name):
    global id_number_list
    id_number_list = []
    for letter in input_name:
        alpha_loc(letter)
        id_number_list.append(location)
    global id_number
    id_number=str(id_number_list[0])    
    for i in range(1,len(id_number_list)):
        id_number+=str(id_number_list[i])
    return id_number
name_id("bob")        



# In[6]:


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def password(input_name_password):
    name_id(input_name_password)
    password= int(id_number)
    subtract_this =0
    for i in id_number:
        if i.isdigit()== True:
            subtract_this += int(i)
    password-=subtract_this
    return password
    


password("bob")


# In[7]:


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def prime_check(prime_input):
    prime_test=0
    if type(prime_input) != int:
        print("Please input an integer")
    elif prime_input==1:
        return "false"
    else: 
        for i in range(2,prime_input):
            if prime_input%i == 0:
                prime_test = 1
                break
        if prime_test == 1:
            return "false"
        else:
            return "true"

num_in = int(input())

prime_check(num_in)


# In[22]:


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:



# -------------------------------------------------------------------------------------- #


def prime_check(num_in):
    prime_test=0
    if num_in==1:
        return "false"
    else: 
        for i in range(2,num_in):
            if num_in%i == 0:
                prime_test = 1
                break
        if prime_test == 1:
            return "false"
        else:
            return "true"



try:
    number_use = int(input("Pick a number!"))
except:
    print("Please input an integer")
    oops+=1

prime_check(number_use)

