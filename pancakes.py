from kitchen import Rosemary
from kitchen.utensils import Bowl, Pan, Plate
from kitchen.ingredients import Flour, Egg, Milk, Salt, Butter

bowl = Bowl.use (name='batter')
pan = Pan.use(name="pancake")
plate = Plate.use()

# Whisking two eggs in a bowl
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
bowl.mix()

# Adding the salt to the eggs
bowl.add (Salt.take('dash'))

# Adding the flower in 5 batches of 50g to the batter
for i in range(5):
    bowl.add (Flour.take('50g'))
    bowl.mix

# Adding the milk 
for i in range(2):
    bowl.add (Milk.take('250ml'))
    bowl.mix

# Cooking the pancakes

for i in range(8):
    # Greasing the pan
    pan.add(Butter.take('bit'))

    # Adding some batter
    pan.add(bowl.take('1/8'))

    # Cooking 1 pancake
    for i in range(4):
        pan.cook()
        pan.flip()

    # Plating 1 pancake
    pancake = pan.take()
    plate.add(pancake)

Rosemary.serve(plate)
