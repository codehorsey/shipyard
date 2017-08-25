class Machine():

    current_container = None

    def load_container(self, container):
        self.current_container = container

    def unload_container(self):
        return self.current_container

    def reset(self):
        self.current_container = None

    def __str__(self):
        return str(self.current_container)
        

class Container():

    type_of_container = 'normal'

    def __str__(self):
        return self.type_of_container

class Truck():

    freight = list()
    limit_of_freight = 10

    def has_room(self):
        return len(self.freight) <= 10

    def load_freight(self, freight):
        self.freight.append(freight)

    def __str__(self):
        return str(len(self.freight))


m = Machine()
c = Container()
t = Truck()

m.load_container(c)

def app(m, c, t):
    if t.has_room():
        # if truck has room for containers
        # get container, load onto truck, reset machine
        container = m.unload_container()
        t.load_freight(container)
        m.reset()


