from cars import Vehicle

# SEDAN
class sedan(Vehicle):
  def __init__(self, seats, model, year, mileage, ID, ownership):
    super().__init__(model, year, mileage, ID, ownership)
    self.seats = 4
