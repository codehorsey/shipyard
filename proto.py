import logging
logging.basicConfig(level=10)
logger = logging.getLogger(__name__)

import random
class Person():

    def __init__(self):
        self.id = random.randrange(1,500)
        self.avoid_items = []
        self.pockets = None

    def pickup_thing(self, thing):
        self.pockets = thing
        
        logger.debug('{} picked up {}.'.format(self.id, thing))
    
    def unload_pockets(self, truck):
        logger.info("{} unloading pockets".format(self.id))
     
        if isinstance(truck, Truck) and truck.eligable_thing(self.pockets):
                logger.debug("Truck accepts {}".format(self.pockets))
                truck.take_thing(self.pockets)
                self.pockets = None
                logger.debug("Pockets are empty")
                return True
        elif not isinstance(truck, Truck):
            logger.error("Wrong class! {} not accepted".format(truck.__class__))
            return False
        else:
            logger.debug("Truck does not accept {}".format(self.pockets))
            return False

class Truck():

    def __init__(self, acceptable_things):
        self.accepts = acceptable_things
        self.inventory = []

    def still_room(self):
        """Checks to see if one or more items can be added
        
        Returns:
            bool: Returns True if any value is more than 0
        """
        values = []
        for k, v in self.accepts.items():
            values.append(v>0)
        return True in values

    def eligable_thing(self, thing):
        """Checks to see if has too many of thing and if thing can be added.
        
        Args:
            thing (TYPE): Thing being checked
        
        Returns:
            bool: True or False if has room and can accept.
        """
        return thing.name in self.accepts and self.accepts[thing.name] > 0

    def take_thing(self, thing):
        """Add thing to inventory and update alloted amount.
        
        Args:
            thing (TYPE): Thing to be added to inventory
        """
        self.inventory.append(thing.name)
        self.accepts[thing.name] -= 1
        logger.debug('Added {} to truck inventory. Room for {} more.'.format(thing, self.accepts[thing.name]))

class Thing():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

apple = Thing('apple')
carrot = Thing('carrot')
watermelon = Thing('watermelon')

normal_load = {'apple':3,'carrot':1}
medium_load = {'apple':2,'carrot':2}
insane_load = {'apple':25,'carrot':13, 'watermelon':10}
heavy_load = {'watermelon':2}
t = Truck(normal_load)
d = Truck(heavy_load)
h = Truck(medium_load)
insanetruck = Truck(insane_load)

p = Person()
helpers = list()

items = ['carrot', 'apple', 'watermelon']
foods = list()

for _ in range(100):
    foods.append(Thing(random.choice(items)))

for _ in range(5):
    helpers.append(Person())

for helper in helpers:
    helper.pickup_thing(random.choice(foods))

def load_the_truck(helpers, truck):
    for helper in helpers:
        '''
        if helper cant unload pockets because truck doesnt accept load
        helper adds thing to list of items to avoid picking up in the future
        helper picks up a new item not of type that didnt work
        '''
        if not helper.unload_pockets(truck):
            helper.avoid_items.append(helper.pockets)
            good_choices = filter(lambda x: x.name not in helper.avoid_items, foods)
           
            try:
                helper.pickup_thing(random.choice(good_choices))
            except IndexError:
                logging.error('No more good_choices')
        else:
            helper.pickup_thing(random.choice(foods))

    
i = 0
while insanetruck.still_room() and i <= 10:
    print i
    load_the_truck(helpers,insanetruck)
    print "----------"
    print insanetruck.accepts
    print "----------"

    i += 1


