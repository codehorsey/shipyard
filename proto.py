import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import random
class Person():

    def __init__(self):
        self.id = random.randrange(1,500)
        self.avoid_items = []

    def pickup_thing(self, thing):
        self.pockets = (thing, thing.name)
        
        logger.debug('{} picked up {}.'.format(self.id, thing))
    
    def unload_pockets(self, truck):
        logger.info("{} unloading pockets".format(self.id))

        if isinstance(truck, Truck) and truck.eligable_thing(self.pockets[1]):
                logger.debug("Truck accepts {}".format(self.pockets[1]))
                truck.take_thing(self.pockets[1])
                self.pockets = None
                logger.debug("Pockets are empty")
                return True
        elif not isinstance(truck, Truck):
            logger.error("Wrong class! {} not accepted".format(truck.__class__))
            return False
        else:
            logger.debug("Truck does not accept {}".format(self.pockets[1]))
            return False


    def unload_thing(self, thing, truck):
        """Attempt to unload thing onto a truck.
        
        Args:
            thing (TYPE): Thing to be unloaded.
            truck (TYPE): Truck to attempt to accept thing.
        """
        logger.info("Person unloading")
        if isinstance(truck, Truck) and truck.eligable_thing(thing):
                logger.debug("Truck accepts {}".format(thing))
                truck.take_thing(thing)
                return True
                
        elif not isinstance(truck, Truck):
            logger.error("Wrong class! {} not accepted".format(truck.__class__))
            return False
        else:
            logger.debug("Truck does not accept {}".format(thing))
            return False

class Truck():

    def __init__(self, acceptable_things):
        self.accepts = acceptable_things
        self.inventory = []

    def eligable_thing(self, thing):
        """Checks to see if has too many of thing and if thing can be added.
        
        Args:
            thing (TYPE): Thing being checked
        
        Returns:
            bool: True or False if has room and can accept.
        """
        return thing in self.accepts and self.accepts[thing] > 0

    def take_thing(self, thing):
        """Add thing to inventory and update alloted amount.
        
        Args:
            thing (TYPE): Thing to be added to inventory
        """
        self.inventory.append(thing)
        self.accepts[thing] -= 1
        logger.debug('Added {} to truck inventory. Room for {} more.'.format(thing, self.accepts[thing]))

class Thing():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

apple = Thing('apple')
carrot = Thing('carrot')
watermelon = Thing('watermelon')

normal_load = {'apple':3,'carrot':1}
heavy_load = {'watermelon':3}
t = Truck(normal_load)
d = Truck(heavy_load)
p = Person()
helpers = list()
import random

items = ['carrot', 'apple', 'watermelon']
foods = list()

for _ in range(50):
    foods.append(Thing(random.choice(items)))

for _ in range(3):
    helpers.append(Person())

for helper in helpers:
    helper.pickup_thing(random.choice(foods))

for helper in helpers:
    if not helper.unload_pockets(t):
        helper.avoid_items.append(helper.pockets)
        good_choice = random.choice(filter(lambda x: x not in helper.avoid_items, foods))
        helper.pickup_thing(good_choice)
