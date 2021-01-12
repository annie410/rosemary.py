from kitchen import Rosemary
from kitchen.utensils import Bowl, Pan, Plate
from kitchen.ingredients import Flour, Egg, Milk, Salt, Butter

bowl = Bowl.use (name='batter')
pan = Pan.use(name="pancake")

# How many pancakes do you want?
n = 8

# Eggs
e = int(0.25*n)

# Flour
f = int(0.625*n)

#  Milk
m = int(0.25*n)


# Whisking two eggs in a bowl
for i in range(0,e):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
bowl.mix()

# Adding the salt to the eggs
bowl.add (Salt.take('dash'))

# Adding the flower in batches of 50g to the batter
for i in range(0,f):
    bowl.add (Flour.take('50g'))
    bowl.mix

# Adding the milk in batches of 250ml
for i in range(0,m):
    bowl.add (Milk.take('250ml'))
    bowl.mix

# Cooking the pancakes
plate = Plate.use()
for i in range(n):
    # Greasing the pan
    pan.add(Butter.take('bit'))

    # Adding some batter
    pan.add(bowl.take(1/n))

    # Cooking 1 pancake
    for i in range(4):
        pan.cook()
        pan.flip()

    # Plating 1 pancake
    pancake = pan.take()
    plate.add(pancake)

Rosemary.serve(plate)
