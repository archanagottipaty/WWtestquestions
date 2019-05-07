from random import randint

def Nthsmallest(myrandomnumbers, n):
   myrandomnumbers.sort()
   print(myrandomnumbers[n - 1])
   print(myrandomnumbers)

myrandomnumbers = []

for x in range(500):
    myrandomnumbers.append(randint(1,1000))


#code to get input from user and check that the value is between 1-500
nthsmallest= input("Enter the nthsmallest number between 1 and 500: ")
while (int(nthsmallest) >500):
    nthsmallest= input("Enter the nthsmallest number between 1 and 500: ")


Nthsmallest(myrandomnumbers, int(nthsmallest))

