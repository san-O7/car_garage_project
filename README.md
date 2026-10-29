# 🚗 Car Management System

A simple **Car Management System** built with Python using Object-Oriented Programming (OOP). This project allows users to add, view, and remove cars from their collection through a command-line interface.

## 📌 Features

- **Add Cars** – Add regular or electric cars to your collection.
- **View Cars** – Display all cars with their details.
- **Remove Cars** – Remove cars by model name (case-insensitive).
- **Electric Cars** – Support for electric vehicles with battery percentage.
- **Duplicate Prevention** – Prevents adding the same car object twice to a user's collection.
- **Car Counter** – Count the total number of cars in a collection.
- **Input Validation** – Handles invalid numeric inputs.

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Command-Line Interface (CLI)

## 🧠 OOP Concepts

This project demonstrates several important OOP concepts:

### 1. Classes and Objects
The program contains four classes:

- `Car` – Represents a regular car with brand, model, year, and price.
- `ElectricCar` – Represents an electric car with an additional battery percentage.
- `User` – Manages a user's personal car collection.
- `Garage` – Provides functionality for storing and managing cars.

### 2. Inheritance
The `ElectricCar` class inherits from the `Car` class, reusing its attributes and adding a battery attribute.

### 3. Method Overriding
The `ElectricCar` class overrides the `__str__()` method to display battery information alongside the car's details.

### 4. Encapsulation
Car management functionality is organized inside classes and accessed through methods such as `add_car()`, `remove_car()`, and `show_cars()`.

## 💻 How to Run

**1. Clone the repository**

```bash
git clone https://github.com/san-O7/your-repository.git
```

**2. Navigate to the project directory**

```bash
cd your-repository
```

**3. Open the Python file and enter your name**

```python
user1 = User("Your Name")
```

**4. Run the program**

```bash
python main.py
```

Make sure Python 3 is installed. No external libraries are required.

## 🎮 Example Usage

When you run the program, the following menu appears:

```text
1 - Add car, 2 - Show cars, 3 - Remove car, 4 - Exit:
```

### Adding a Car

```text
Enter brand: Tesla
Enter model: Model 3
Enter year: 2023
Enter price: 35000
Is your car electric? (yes/no) yes
Enter battery %: 85

Added the car Successfully
```

### Viewing Cars

```text
Brand: Tesla, Model: Model 3, Year: 2023, Price: 35000, Battery: 85%
```

### Removing a Car

```text
The model you'd like to remove: Model 3

Removed the car successfully
```

## 📂 Project Structure

```text
Car-Management-System/
│
├── main.py
└── README.md
```

## 🚀 Future Improvements

- Save and load cars using JSON files.
- Add a search feature for cars.
- Implement car sorting by price or year.
- Add validation for battery percentage, year, and price.
- Connect the `Garage` class to the interactive menu.
- Build a graphical user interface (GUI).

## 📖 About the Project

This project was created to practice **Python Object-Oriented Programming**, including classes, inheritance, method overriding, constructors, and working with lists of objects.

It also provides experience with user input, loops, conditional statements, and exception handling.
