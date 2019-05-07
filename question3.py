#I will generate random numbers using randint and then populate a list 
# I will sort the list and that will make it easy to find any value using it's position in the list

from random import randint

def Nthsmallest(myrandomnumbers, n):
   myrandomnumbers.sort()
   print(myrandomnumbers[n - 1])
 
#list that will contain the random numbers
myrandomnumbers = []

for x in range(500):
    myrandomnumbers.append(randint(1,1000))


#code to get input from user and check that the value is between 1-500
nthsmallest= input("Enter the nthsmallest number between 1 and 500: ")
while (int(nthsmallest) >500):
    nthsmallest= input("Enter the nthsmallest number between 1 and 500: ")


Nthsmallest(myrandomnumbers, int(nthsmallest))

