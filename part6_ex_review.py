#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
print(s[0])
# 'o'
print(s[-1])
# 'djan'
print(s[:4])
# 'jan'
print(s[1:4]) # Indexes 0-6 s[start,upto-but-not-included]
# 'go'
print(s[4:])
# Bonus: Use indexing to reverse the string
i =len(s) - 1
#print(s)
while i >= 0:
	print(s[i], sep=' ', end='', flush=True)
	i -= 1

# Or
print(f"\nPrint reverse of list: {s[::-1]}")

###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
l[2][2] = "goodbye"
print(f"\nNested List: {l}")

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print(f"\nDictionary_1dim: {d1['simple_key']}")
d2 = {'k1':{'k2':'hello'}}
print(f"\nNested dictionary: {d2['k1']['k2']}")
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(f"\nNested dictionary: {d3['k1'][0]['nest_key'][1][0]}")

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

myset = set(mylist)
print(f"\n\t myset: {myset}")

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

print(f"Hello my dog\'s name is {name} and he is {age} years old") 

print("\n--------------- Program Completed! ---------------\n")