import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Person():

    def __init__(self):
        pass

    def pickup_thing(self, thing):
        self.pockets = thing
        logger.debug('Person picked up {}.'.format(thing))
    
    def unload_pockets(self, truck):
        logger.info("Person unloading pockets")
        if isinstance(truck, Truck) and truck.eligable_thing(self.pockets):
                logger.debug("Truck accepts {}".format(self.pockets))
                truck.take_thing(self.pockets)
                self.pockets = None
                logger.debug("Pockets are empty")
        elif not isinstance(truck, Truck):
            logger.error("Wrong class! {} not accepted".format(truck.__class__))
        else:
            logger.debug("Truck does not accept {}".format(self.pockets))


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
                
        elif not isinstance(truck, Truck):
            logger.error("Wrong class! {} not accepted".format(truck.__class__))
        else:
            logger.debug("Truck does not accept {}".format(thing))

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

normal_load = {'apple':3,'carrot':1}
heavy_load = {'watermelon':3}
t = Truck(normal_load)
d = Truck(heavy_load)
p = Person()

p.unload_thing('ban', t)
p.unload_thing('carrot', t)
p.unload_thing('apple', t)
p.unload_thing('apple', t)
p.unload_thing('apple', t)
p.unload_thing('apple', t)
p.unload_thing('apple', d)

p.pickup_thing('watermelon')
p.unload_pockets(t)
p.unload_pockets(d)

print p.pockets
print t.inventory