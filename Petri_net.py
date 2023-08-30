class PetriNet():

    def __init__(self):
        self.places = []
        self.transitions = []
        self.flow = []
        self.token = []
    def add_place(self, name):
        self.places.append((name,0))
        

    def add_transition(self, name, id):
        self.transitions.append((name,id))

    def add_edge(self, source, target):
        self.flow.append[(source,target)]

    def get_tokens(self, place):
        for place in self.places:
            if place[0] == 1:
                print(place[1])

    def is_enabled(self, transition):
        for t in self.transition:
            if t[1] == transition:
                for place in places:
                    if pl

    def add_marking(self, place):
        for place in self.places:
            if place[0] == 1:
                place += 1

    def fire_transition(self, transition):
        # code here

# etc
p = PetriNet()

p.add_place(1)  # add place with id 1
p.add_place(2)
p.add_place(3)
p.add_place(4)
p.add_transition("A", -1)  # add transition "A" with id -1
p.add_transition("B", -2)
p.add_transition("C", -3)
p.add_transition("D", -4)

p.add_edge(1, -1)
p.add_edge(-1, 2)
p.add_edge(2, -2).add_edge(-2, 3)
p.add_edge(2, -3).add_edge(-3, 3)
p.add_edge(3, -4)
p.add_edge(-4, 4)

print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

p.add_marking(1)  # add one token to place id 1
print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

p.fire_transition(-1)  # fire transition A
print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

p.fire_transition(-3)  # fire transition C
print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

p.fire_transition(-4)  # fire transition D
print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

p.add_marking(2)  # add one token to place id 2
print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

p.fire_transition(-2)  # fire transition B
print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

p.fire_transition(-4)  # fire transition D
print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

# by the end of the execution there should be 2 tokens on the final place
print(p.get_tokens(4))
