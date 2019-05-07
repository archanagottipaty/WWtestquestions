def doesFileExist(string):
    try:
        f = open(string,"r")
    except FileNotFoundError:
        print("This file does not exist")

doesFileExist("Myinputfile.txt")
f=open("Myinputfile.txt","r")

for line in f:
    output=(line.split("-"))
    print(output[0].lstrip())
    output2=(output[1].split(","))
    for x in output2:
        print(x.lstrip().rstrip()) #lstrip() removes leading whitespace and rstrip() removes trailing newlines
