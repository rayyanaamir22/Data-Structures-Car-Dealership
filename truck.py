from cars import Vehicle

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
