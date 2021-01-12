from kitchen.utensils.Utensil import PieDish
from kitchen import Rosemary
from kitchen.utensils import Bowl, Oven, Plate, BakingTray, Fridge
from kitchen.ingredients import Flour, Egg, Salt, Butter, Sugar, BakingPowder, Water, Apple, Lemon, Cornstarch, Cinnamon

oven = Oven.use()
fride = Fridge.use()

#Chill some water
bowl = Bowl.use (name='water')
bowl.add(Water.take('200mL'))
fride.use(bowl)

#Remember to preheat the oven before we start
oven.preheat(degrees=180)


#Make the dough

bowl2 = Bowl.use (name='dough')
bowl2.add(Flour('300g'))
bowl2.add(Salt('teaspoon'))
bowl2.mix()

#Add butter
for i in range(5):
    bowl.add (Butter.take('50g'))
    bowl.mix

#Add the water
for i in range(8):
    bowl2.add(bowl.take(1/8))
    bowl2.mix()

#Chill the batter in the fridge
fride.use(bowl2)


#Make the filling

bowl3= Bowl.use (name='filling')
apple = Apple.take()
lemon = Lemon.take()

#Peel & Slice the apples
for i in range(6):
    apple.peel()
    apple.slice()
    bowl3.add

#Zest & Juice the lemon
lemon.zest()
lemon.squeeze()
bowl3.add

#Add the rest
bowl3.add(Sugar.take('150g'))
bowl3.add(Cornstarch.take('Spoonful'))
bowl3.add(Salt.take('pinch'))
bowl3.add(Cinnamon.take('teaspoon'))
bowl3.mix()

#Put it in the dish
pie_dish = PieDish.use (name='Pie')
pie_dish.add(bowl2.take(3/4))
pie_dish.add(bowl3.take())
pie_dish.add(bowl2.take(1/4))

#Egg wash
bowl4 = Bowl.use()
egg = Egg.take()
egg.crack()
bowl4.add(egg)
bowl4.mix()

# Putting the egg wash on the pie
pie_dish.add(bowl4.take())
pie_dish.add(Sugar.take('spoon'))
pie_dish.add(lemon.take(1/4))

# Put the dish in the oven and bake
oven.add(pie_dish)

oven.bake(60)

#Take the pie out of the oven
oven.take()

ApplePie = pie_dish.take()

#Plate the pie
plate = Plate.use()
plate.add(ApplePie)

Rosemary.serve(plate)





