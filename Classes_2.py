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
    
shona = Carpet('Dash','Belgium','Saddle')

shona.desire('Plum')