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
    type_of_containers = {0:'normal', 1:'heavy', 2:'refridge'}

    def __init__(self, container_type=0):
        
        self.type_of_container = self.type_of_containers[container_type]

    def __str__(self):
        return self.type_of_container

class Truck():

    def __init__(self, accepted_loads):
        self.freight = list()
        self.accepts = dict()

        self.accepts['normal'] = accepted_loads[0]
        self.accepts['heavy'] = accepted_loads[1]
        self.accepts['refridge'] = accepted_loads[2]

    def has_room(self):
        return len(self.freight) <= 3

    def load_freight(self, freight):
        self.freight.append(freight)

    def __str__(self):
        return str(len(self.freight))


normal_load = [3,0,0]
heavy_load = [0,3,0]
refridgerated_load = [0,0,3]
mixed_load = [1,1,0]

m = Machine()
c = Container(0)
t = Truck(normal_load)
tt = Truck(heavy_load)
h = Container(1)

def app(m, c, t):
    m.load_container(c)      

    if t.accepts[c.type_of_container] > 0:
        # if truck accepts type of container


        # get container, load onto truck, minus inventory, reset machine
        container = m.unload_container()
        t.load_freight(container)
        t.accepts[container.type_of_container] -= 1
