# 📘 Assignment: Python Classes

## 🎯 Objective

Learn how to define and use classes in Python to model real-world objects and behaviors.

## 📝 Tasks

### 🛠️ Define a Simple Class

#### Description
Create a class named `Car` that represents a car with attributes for make, model, and year. Add a method to display information about the car.

#### Requirements
Completed program should:

- Define a class `Car` with `make`, `model`, and `year` attributes
- Include a method `display_info()` that prints the car's details
- Create an instance of `Car` and call `display_info()`

#### Example
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

car = Car("Toyota", "Camry", 2022)
car.display_info()  # Output: 2022 Toyota Camry
```


### 🛠️ Add Methods and Interactions

#### Description
Expand the `Car` class to include a method to update the car's mileage and another to display the current mileage.

#### Requirements
Completed program should:

- Add a `mileage` attribute to the `Car` class (default 0)
- Add a method `update_mileage(new_mileage)` to update the mileage
- Add a method `display_mileage()` to print the current mileage
- Demonstrate updating and displaying mileage for a `Car` instance

#### Example
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
    
    def update_mileage(self, new_mileage):
        self.mileage = new_mileage
    
    def display_mileage(self):
        print(f"Mileage: {self.mileage} miles")

car = Car("Toyota", "Camry", 2022)
car.update_mileage(15000)
car.display_mileage()  # Output: Mileage: 15000 miles
```
