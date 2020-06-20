class Car():
    
    
    def __init__(self, model, color, pos):
        self.model = model
        self.color = color
        self.pos = pos
        
        
    def printCar(self):
        print('My car is {} model and its color is {} and is at {}'.format(self.model, self.color, self.pos))
        
    
    def MoveCar (self, a):
        self.pos+=a
        
        
        
    
p = Car('1984', 'blue', 2)
p.MoveCar(6)
p.printCar()
