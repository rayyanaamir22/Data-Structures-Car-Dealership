from cars import Vehicle

# SPORTS CAR
class sportsCar(Vehicle):
  def __init__(self, seats, convertible, model, year, mileage, ID, ownership):
    super().__init__(model, year, mileage, ID, ownership)
    self.seats = 2
    self.convertible = False

  def roof(self):
    self.convertible = True
