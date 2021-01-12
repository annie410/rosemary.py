from kitchen import Rosemary
from kitchen.utensils import Bowl, Oven, Plate, BakingTray
from kitchen.ingredients import Flour, Egg, Salt, Butter, Sugar, ChocolateChips, BakingPowder

# How many cookies do you want?
n = 16

# Eggs given desired number of cookies
e = int(0.125*n)

# Flour given desired number of cookies
f = int(0.375*n)

# Butter and Chocolate Chips given desired number of cookies
b = int(12.5*n)

# Sugar given desired number of cookies
s = int(0.25*n)

oven = Oven.use()

#Remember to preheat the oven before we start
oven.preheat(degrees=175)


bowl = Bowl.use (name='batter')
# Cream together the butter and the sugar 
bowl.add(Butter.take(grams=b))
for i in range(0, s):
    bowl.add(Sugar.take('50g'))
    bowl.mix()

# Mix in each egg
for i in range(0, e):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
    bowl.mix()

# Add the salt and chocolate chips
bowl.add(Salt.take('pinch'))
bowl.add(ChocolateChips.take(grams=b))

#Add the flour in stages
for i in range(0, f):
    bowl.add (Flour.take('50g'))
    bowl.mix()

#Add the baking soda
bowl.add(BakingPowder.take('some'))

#Mix it all together one last time for good luck
bowl.mix()


tray = BakingTray.use (name='cookies')

#Put cookies on the baking tray
for i in range(0, n):
    tray.add(bowl.take(1/n))

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