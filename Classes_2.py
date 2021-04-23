# Instance Variables

class Carpet:
    # Constructor Method
    def __init__(self,name,place,colour):
        self.name = name
        self.place=place
        self.colour=colour
    # Instance Method
    def desire(self,new_colour):
        print(f'First Colour picked was {self.colour}')
        self.new_colour = new_colour
        print(f'Desired Colour was {self.colour}')
    
# shona = Carpet('Dash','Belgium','Saddle')

# shona.desire('Plum')

# An object is an instance of class

class Target:
    def skip(self):
        print('Dash to moon in one leap !')
# Here moon is an instance of the class Target
# moon = Target()
# moon.skip()


class Automobile:
    vehicle_type = 'Personal'
    # Constructor Methods
    def __init__(self,name,speed,CC,people):
        self.name=name
        self.speed = speed
        self.CC=CC
        self.people=people
    # Instance Methods
    """ I attached a nitro system to my car
    this would boost my car's speed by 50 %  """
    def Nitro(self):
        boost = 1.5
        return f'This would turn my car to zip at {self.speed*1.5} KMPH'

mobile1 = Automobile('Needle',240,'3400',4)
#print(mobile1.Nitro())

# To view the assigned values as key and pair we can do it by
#print(mobile1.__dict__)

# print(mobile1.__init__('Tail',360,456,3)) # Calling it explicitly from the instance overrides the created instance

# print(mobile1.Nitro()) # This would turn my car to zip at 540.0 KMPH

# Calling the static variable from the class instance
# print(mobile1.vehicle_type)
