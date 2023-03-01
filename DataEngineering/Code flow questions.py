#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:


for i in range(0,5):
    print(x[i])


# In[3]:


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for i in range(0,len(x)):
    if x[i]%2 ==0:
        print(x[i])


# In[4]:


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:

for i in range(0,4):
    if x[i]%2 ==0:
        print(x[i])


# In[5]:


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
first_letter = []
for i in names:
    first_letter.append(i[0])
print(first_letter)




# In[6]:


print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
space_index = []
for i in names:
    location=i.find(' ')
    space_index.append(location)
print(space_index)
    




# In[7]:


print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
first_letter = []
first_letter_surname = []
for i in names:
    first_letter.append(i[0])
    location=i[(i.find(' '))+1]
    first_letter_surname.append(location)
print_name=[]
for i in range(0,len(first_letter)):
    initials = first_letter[i] + first_letter_surname[i]
    print_name.append(initials)
print(print_name)




# In[8]:


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:
list_of_sets=[]
for list in list_of_lists:
    if len(set(list)) == len(list):
        print(list)


# In[5]:


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
in_test = 0
while in_test <= float(100):
    try:
        in_test = float(input('Enter a number over 100!'))
        
    except:
        print('That\'s not a number! Please Enter a number over 100')
    
else:
    print(in_test)


# In[15]:


print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

in_test = 0
prime_check = 0
while in_test <= 100:
    try:
        in_test = int(input('Enter a number over 100!'))
        
    except:
        print('That\'s not a number! Please Enter a number over 100')
    
else:
    print(in_test) 
    for i in range(2,in_test):
        if in_test%i == 0:
            prime_check = 1
            break
    if prime_check == 1:
        print("not prime")
    else:
        print("prime")

