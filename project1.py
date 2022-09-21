# 1  2  3  4  5
# 6  7  8  9  10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

from ast import In
import sys
#variables
counter = 0
pathNumber = 0
path1 = ""
#data
data = """1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25"""
print(data)

#start and finish
startNumber = int(input("enter start number: "))
endNumber = int(input("enter end number: "))
pathNumber = startNumber
#user second path
def everythingElse():
    print(data)
    #print("you are currently at number " + str(pathNumber) + ". This step is step #" + str(counter) + ".")
    path = input("would you like to go left, down-left, down, down-right, or right?: ")
    if path ==  "left":
        left()
        outers()
    elif path == "down":
        down()
        outers()
    elif path == "down-left":
        downLeft()
        outers()
    elif path =="right":
        right()
        outers()
    elif path == "down-right":
        downRight()
        outers()
    else:
        print("error input - please try again")
        outers()
#right function
def right():
    global counter
    global pathNumber
    counter = counter + 1
    pathNumber = pathNumber + 1
    completion()

#left function
def left():
    global counter
    global pathNumber
    counter = counter +1
    pathNumber = pathNumber -1
    completion()

#down function
def down():
    global counter
    global pathNumber
    counter = counter +1
    pathNumber = pathNumber +5
    completion()

#downLeft function
def downLeft():
    global counter
    global pathNumber
    counter = counter +1
    pathNumber = pathNumber +4
    completion()

#downRight function
def downRight():
    global counter
    global pathNumber
    counter = counter +1
    pathNumber = pathNumber +6
    completion()

#check for completion
def completion():
    if pathNumber == endNumber:
        print("Congratulations! you got to your number in " + str(counter) + " step(s)!")
    else:
        print(data)
        outers()
        
#user outer path
def outers():
    print("you are currently at number " + str(pathNumber) + ". This step is step #" + str(counter) + ".")
    if pathNumber == 1 or pathNumber == 6 or pathNumber == 11 or pathNumber == 16 or pathNumber == 21:
        path = input("would you like to go right, down, or down-right? ")
        if path ==  "right":
            right()
        elif path == "down":
            down()
        elif path == "down-right":
            downRight()
        else:
            print("error input - please try again")
            outers()
    elif pathNumber == 5 or pathNumber == 10 or startNumber == 15 or pathNumber == 20 or pathNumber == 25:
        path = input("would you like to go left, down, or down-left?")
        if path ==  "left":
            left()
        elif path == "down":
            down()
        elif path == "down-left":
            downLeft()
        else:
            print("error input - please try again")
            outers()
    else:
        everythingElse()
outers()