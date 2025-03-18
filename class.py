class Car:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model

  def show_details(self):
    print(f"car brand: {self.brand} , car model: {self.model}")

car1 = Car("tesla","kuch")
car2 = Car("bmw","m4")


car1.show_details()
car2.show_details()