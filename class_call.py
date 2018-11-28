"""
This program calls two custom classes.  It also shows the syntax for the
for-loop and while-loop.
"""

# Import classes from your custom package
# from <dir.file = package.module> import <class_name | method (case sensitive)>
from Animals.Mammals import *
from Animals.Pajaros import Birds
# Get system info
from socket import *
import platform
import Person # Importing custom module can't be found or is not callable???

''' import call to object only works with packages from standard library '''
#import Birds
 
# Create an object of Mammals class & call a method of it
myMammal = Mammals()
myMammal.printMembers()
 
# Create an object of Birds class & call a method of it
myBird = Birds()
myBird.printMembers()

# Three ways to print
print(f"\nLocal Platform:")
# Print fully qualified hostname
print("\n\tHostname: %s \n\tPlatform: %s %s\n" % (getfqdn(), platform.system(), platform.release()))
# New style of formatting, you can omit the index #
print("\n\tHostname: {0} \n\tPlatform:{1} {2}\n".format(getfqdn(), platform.system(), platform.release()))
# New in Python 3.6
print(f"\n\tHostname: {getfqdn()} \n\tPlatform:{platform.system()} {platform.release()}\n")

# Instantiated p1 Object
#p1 = Person("Sylvester      Stalone", "19460706")

#print(f"\nName: {p1.last_name} \nDOB: {p1.birthday}")

# ---------------------------- End of Custom Class calls -------------------------------

print("======= First for-loop =========")

# for i in range(start, end, increment):
for y in range(0,100,10): # 0 - 90
    print(y)

print("\n======= Second for-loop =========")
# for i in range(end, start, decrement):
for x in range(100,1,-20): # 100 - 20
    print(x)

print("\n======= Right triangle =========")
for j in range(0,10,1): # 0 - 9
    #print(f'{j}*')
    print()
#else:
#    print("End of for-loop")
    i = 0
    while i <= j:
        print('*', sep=' ', end='', flush=True)
        i += 1
    #else:
    #    print("End of while loop")

print("\n======= Rectangle =========")
for out in range(0,5,1):
    inner = 10
    s = 0
    print() # Starts printing on next like for while loop print
    while s <= inner:
        print('*', sep='H ', end='M', flush=True)
        s += 1
#range(start,end,increment)
print(f"\n\nRange function:")
for i in range(1,5,1):
    print(i)
print("\n--------------- Program Completed! ---------------\n")