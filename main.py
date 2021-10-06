from Page1 import Page1
from Page2 import Page2
from rewardnote import rewardnote


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
