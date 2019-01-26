# A dice roller that works with any combo of dice and sides.

import re
import random

def diceRoll():
    print("Type rolls with form 'XdY' where X is number of dice and Y is number of sides.")
    print("Type exit to quit at anytime")
    roll = ""
    while roll != "exit":
        roll = input("enter a dice to roll in the form of XdY: ").lower()
        total = 0
        while re.search("\d+d\d+",roll) == None and roll != "exit":
            roll = input("Please re-enter with form XdY: ")
        if roll == "exit":
            print("goodbye")
            return
        splitNums = roll.split("d")
        dice = int(splitNums[0])
        sides = int(splitNums[1])
        while dice > 0:
            throw = random.randint(1,sides)
            if dice > 1:
                print(throw, end=' + ')
            else:
                print(throw, end= ' = ')
            total += throw
            dice -= 1
            
        print(total)

diceRoll()

