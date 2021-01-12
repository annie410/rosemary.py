from kitchen import Rosemary
from kitchen.utensils import Bowl, Oven, Plate, BakingTray
from kitchen.ingredients import Flour, Egg, Salt, Butter, Sugar, ChocolateChips, BakingPowder

oven = Oven.use()

#Remember to preheat the oven before we start
oven.preheat(degrees=175)

bowl = Bowl.use (name='batter')
# Cream together the butter and the sugar 
bowl.add(Butter.take("200g"))
for i in range(4):
    bowl.add(Sugar.take('50g'))
    bowl.mix()

# Mix in each egg
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
    bowl.mix()

# Add the salt and chocolate chips
bowl.add(Salt.take('pinch'))
bowl.add(ChocolateChips.take('200g'))

#Add the flour in stages
for i in range(6):
    bowl.add (Flour.take('50g'))
    bowl.mix()

#Add the baking soda
bowl.add(BakingPowder.take('some'))

#Mix it all together one last time for good luck
bowl.mix()

tray = BakingTray.use (name='cookies')

#Put 16 cookies on the baking tray
for i in range(16):
    tray.add(bowl.take(1/16))

#Put the tray in the oven
oven.add(tray)

#Bake the cookies
oven.bake(10)

#Take the cookies out of the oven
oven.take()

cookies = tray.take()

#Plate the cookies
plate = Plate.use()
plate.add(cookies)

Rosemary.serve(plate)