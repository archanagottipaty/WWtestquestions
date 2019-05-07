from random import randint

def Nthsmallest(myrandomnumbers, n):
   myrandomnumbers.sort()
   print"The %dth smallest value is:" %n,myrandomnumbers[n - 1]


myrandomnumbers = []

for x in range(500):
    myrandomnumbers.append(randint(1,1000))


nthsmallest= input("Enter the nth smallest number between 1 and 500: ")
while (int(nthsmallest) > 500) or (int(nthsmallest) < 1):
    nthsmallest= input("Enter the nth smallest number between 1 and 500: ")


Nthsmallest(myrandomnumbers, int(nthsmallest))
