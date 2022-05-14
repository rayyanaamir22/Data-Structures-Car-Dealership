from cars import Vehicle

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
