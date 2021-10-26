# The user can choose the word list he/she wishes to practice 
# After practicing certain amount of words each day, the number of learned words will be transfered into the same amount of food to "feed" the pet as reward
# This sample only provides the process for a user to open and use the software for the first time to learn the words
"""Pick the CET4_edited.txt, CET6_edited.txt, TOEFL_abridged.txt as example data to enable to user to choose 
(vocabulary list resource: https://github.com/mahavivo/english-wordlists), """



from Page1 import Page1
from Page2 import Page2
from rewardnote import rewardnote
from Page4 import Page4
from Page5 import Page5Cat, Page5Dog

p1 = Page1()
p2 = Page2()


Page1.select_channel(p1)
goal = p2.getgoal(p2)
choice = Page1.getchoice()
print(choice, goal)

rewardnote()

from Page3 import Page3
p3 = Page3()
tageswords = p3.select_channel(goal, str(choice))

p4 = Page4()
name, pet= p4.select_channel(p4)

from Page6 import food
p6 = food()
p6.select_channel(name, pet, goal)

