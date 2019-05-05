from random import randint

def Nthsmallest(myrandomnumbers, n):
   myrandomnumbers.sort()
   print(myrandomnumbers[n - 1])
   print(myrandomnumbers)

myrandomnumbers = []

for x in range(500):
    myrandomnumbers.append(randint(1,1000))

Nthsmallest(myrandomnumbers, 7)

