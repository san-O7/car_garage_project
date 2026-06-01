class Car:
    
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
    
    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Price: {self.price}"

class ElectricCar(Car):
    def __init__(self, brand, model, year, price, battery):
        super().__init__(brand, model, year, price)
        self.battery = battery

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Price: {self.price}, Battery: {self.battery}%"
    

class User:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        if car not in self.cars:
            self.cars.append(car)
            print("Added the car Successfully")
        else:
            print("You already own this car")

    def show_cars(self):
        if not self.cars:
            print("No cars")
        else:
            for car in self.cars:
                print(car)

    def remove_car(self, model):
        found = False
        for car in self.cars.copy():
            if model.lower() == car.model.lower():
                self.cars.remove(car)
                found = True

        if found:
            print("Removed the car successfully")
        elif len(self.cars) ==  0:
            print("No cars")
        else:
            print("Couldn't find the car")

    def car_count(self):
        return len(self.cars)

class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print("Added the car Successfully")

    def show_cars(self):
        for car in self.cars:
            print(car)

    def remove_car(self, model):
        found = False
        for car in self.cars.copy():
            if model.lower() == car.model.lower():
                self.cars.remove(car)
                found = True

        if found:
            print("Removed the car successfully")
        else:
            print("Couldn't find the car")

    def car_count(self):
        return len(self.cars)

# Add your name here
user1 = User("")

garage1 = Garage()


def menu():
    loop = True
    while loop == True:
        try:
            choice = int(input("1 - Add car, 2 - Show cars, 3 - Remove car, 4 - Exit: "))

            if choice == 1:
                try:
                    brand = input("Enter brand: ")
                    model = input("Enter model: ")
                    year = int(input("Enter year: "))
                    price = int(input("Enter price: "))

                    is_electric = input("Is your car electric? (yes/no) ").lower()

                    if is_electric == "yes":
                        battery = int(input("Enter battery %: "))
                        new_car = ElectricCar(brand.capitalize(), model.capitalize(), year, price, battery)
                    else:
                        new_car = Car(brand.capitalize(), model.capitalize(), year, price)

                    user1.add_car(new_car)

                except ValueError:
                    print("Invalid input. Please enter numbers where required.")

            elif choice == 2:
                user1.show_cars()

            elif choice == 3:
                model_choice = input("The model you'd like to remove: ")
                user1.remove_car(model_choice)

            elif choice == 4:
                loop = False
                print("You've exited")
        except ValueError:
            print("Please enter a valid number")
menu()



