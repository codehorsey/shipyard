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
    type_of_containers = ('normal', 'heavy', 'refridge')
    type_of_container = 'None'

    def __init__(self, container_type=0):
        # 0 = Normal 1 = Heavy 2 = Redrige
        self.type_of_container = self.type_of_containers[container_type]

    def __str__(self):
        return self.type_of_container

class Truck():

    def __init__(self, n,h,r):
        self.freight = list()
        self.accepts = dict()

        self.accepts['normal'] = n
        self.accepts['heavy'] = h
        self.accepts['refridge'] = r

    def has_room(self):
        return len(self.freight) <= 3

    def load_freight(self, freight):
        self.freight.append(freight)

    def __str__(self):
        return str(len(self.freight))


m = Machine()
c = Container(0)
t = Truck(2,0,0)
tt = Truck(0,5,2)
h = Container(1)

def app(m, c, t):
    m.load_container(c)      

    if t.accepts[c.type_of_container] > 0:
        # if truck accepts type of container


        # get container, load onto truck, minus inventory, reset machine
        container = m.unload_container()
        t.load_freight(container)
        t.accepts[container.type_of_container] -= 1
