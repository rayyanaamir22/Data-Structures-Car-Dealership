# CARS 

# Create vehicle class
class Vehicle(object):
  def __init__(self, seats, model, year, mileage, ID, ownership = False):
    self.seats = seats
    self.model = model
    self.year = year
    self.mileage = mileage
    self.ID = ID
    self.ownership = False 
          
  
  def buyout(self):
    self.ownership = True
    
  
  def lease(self):
    self.ownership = True

  
  def sell(self):
    self.ownership = False
  

# CREATE DEFAULT VEHICLE INSTANCES

# SEDAN
class sedan(Vehicle):
  def __init__(self, seats, model, year, mileage, ID, ownership):
    super().__init__(model, year, mileage, ID, ownership)
    self.seats = 4

# SUV
class SUV(Vehicle):
  def __init__(self, seats, model, year, mileage, ID, ownership):
    super().__init__(model, year, mileage, ID, ownership)
    self.seats = 5
    global sevenSeaterMode
    sevenSeaterMode = False
  
  def sevenSeater(self): # Convert to 7 seater
    sevenSeaterMode = True
    self.seats = 7

  def fiveSeater(self): # Convert to 5 seater
    sevenSeaterMode = False
    self.seats = 5


# TRUCK
class truck(Vehicle):
  def __init__(self, seats, load, model, year, mileage, ID, ownership):
    super().__init__(model, year, mileage, ID, ownership)
    self.seats = 5
    self.load = False

  def hasLoad(self): # Add load
    self.load = True

  def removeLoad(self): # Remove load
    self.load = False

# SPORTS CAR
class sportsCar(Vehicle):
  def __init__(self, seats, convertible, model, year, mileage, ID, ownership):
    super().__init__(model, year, mileage, ID, ownership)
    self.seats = 2
    self.convertible = False

  def roof(self):
    self.convertible = True