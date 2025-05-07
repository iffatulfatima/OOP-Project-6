#1:   Using self
# Assignment:1
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values 
# via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name      
        self.marks = marks    

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


student1 = Student("Iffat", 75)
student1.display()

# 2. Using cls
# Assignment:2
# Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0  # Class variable to keep track of number of objects

    def __init__(self):
        Counter.count += 1  # Increment count each time an object is created

    @classmethod
    def show_count(cls):
        print("Total objects created:", cls.count)

# Example usage
obj1 = Counter()
obj2 = Counter()


Counter.show_count()

# 3. Public Variables and Methods
# Assignment:3
# Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):        # Public method
        print(f"The {self.brand} car has started.")

# Instantiate the class
my_car = Car("Civic")

# Access public variable
print("Car Brand:", my_car.brand)

# Access public method
my_car.start()


# 4. Class Variables and Class Methods
# Assignment:4
# Create a class Bank with a class variable bank_name.
#  Add a class method change_bank_name(cls, name) that allows changing the bank name.
#  Show that it affects all instances.

class Bank:
    bank_name = "National Bank"  # Class variable shared by all instances

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

# Create instances
acc1 = Bank("Iffat")
acc2 = Bank("Fatima")

# Display initial bank name
acc1.display()
acc2.display()

# Change bank name using class method
Bank.change_bank_name("Metropolitan Bank")

# Display updated bank name
acc1.display()
acc2.display()

# 5. Static Variables and Static Methods
# Assignment:5
# Create a class MathUtils with a static method add(a, b) that returns the sum.
#  No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Using the static method without creating an object
result = MathUtils.add(20, 10)
print("Sum:", result)

# 6. Constructors and Destructors
# Assignment: 6
# Create a class Logger that prints a message when an object is created (constructor) and another message
#  when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger initialized: Object created.")

    def __del__(self):
        print("Logger terminated: Object destroyed.")

# Create an object
log = Logger()

# Optional: force object deletion (for demonstration)
del log

# 7. Access Modifiers: Public, Private, and Protected
# Assignment:7
# Create a class Employee with:a public variable name,a protected variable _salary, and
# a private variable __ssn.# Try accessing all three variables from an object
#  of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public
        self._salary = salary    # Protected (by convention)
        self.__ssn = ssn         # Private

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

# Create an object
emp = Employee("Fatima", 30000, "0000-45-2345")

# Access public variable
print("Public - Name:", emp.name)  # ✅ Allowed

# Access protected variable
print("Protected - Salary")


# 8. The super() Function
# Assignment:8
# Create a class Person with a constructor that sets the name. 
# Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

# Base class
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor: Name is {self.name}")

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call base class constructor
        self.subject = subject
        print(f"Teacher constructor: Subject is {self.subject}")

# Example usage
t1 = Teacher("Iffat", "Mathematics")


#  Abstract Classes and Methods
# Assignment:9
# Use the abc module to create an abstract class Shape with an abstract method area(). 
# Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method, no implementation

# Derived class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage
rect = Rectangle(5, 4)
print("Area of Rectangle:", rect.area())


# 10. Instance Methods
# Assignment:10
# Create a class Dog with instance variables name and breed.
#  Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name      # Instance variable
        self.breed = breed    # Instance variable

    def bark(self):           # Instance method
        print(f"{self.name} says: Woof woof!")

# Example usage
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()


# 11. Class Methods
# Assignment:11
# Create a class Book with a class variable total_books. 
# Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0  # Class variable to track total number of books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Increase the book count when a new book is added

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def show_total_books(cls):
        print(f"Total books: {cls.total_books}")

# Example usage
bbook1 = Book("اُردو کی آخری کتاب", "ابنِ انشاء")
book2 = Book("خدیجہ تُل کُبرٰی", "قاضی ساجد")
book3 = Book("زاویہ", "اشفاق احمد")

# Show total number of books
Book.show_total_books()


# 12. Static Methods
# Assignment:12
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that 
# returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage
celsius = 32
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")


# 13. Composition
# Assignment:13
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class
# during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def __init__(self, model, horsepower):
        self.model = model
        self.horsepower = horsepower

    def start(self):
        return f"Engine {self.model} with {self.horsepower} horsepower started."

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has an Engine object

    def start_car(self):
        return f"{self.make} {self.model} - {self.engine.start()}"  # Access Engine method through Car

# Example usage
engine1 = Engine("V8", 400)
car1 = Car("Ford", "Mustang", engine1)

# Start the car and access engine method via Car
print(car1.start_car())

# 14. Aggregation
# Assignment:14
# Create a class Department and a class Employee. Use aggregation by having a Department object store a 
# reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        return f"Employee: {self.name}, Position: {self.position}"

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  # This will hold references to Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_department(self):
        print(f"Department: {self.dept_name}")
        for employee in self.employees:
            print(employee.display_info())

# Example usage
emp1 = Employee("Ali", "Manager")
emp2 = Employee("Iffat", "Developer")

dept = Department("IT")
dept.add_employee(emp1)
dept.add_employee(emp2)

# Display department and its employees
dept.display_department()


# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:15
# Create four classes:
"""A with a method show(),
B and C that inherit from A and override show(),
D that inherits from both B and C.
Create an object of D and call show() to observe MRO."""

class A:
    def show(self):
        print("Class A: show() method")

class B(A):
    def show(self):
        print("Class B: show() method")

class C(A):
    def show(self):
        print("Class C: show() method")

class D(B, C):
    pass

# Create an object of D and call show()
d = D()
d.show()

# Display the MRO for class D
print("MRO for class D:", D.mro())


# 16. Function Decorators
# Assignment:16
# Write a decorator function log_function_call that prints "Function is being called" before 
# a function executes. Apply it to a function say_hello().

# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

# Function to be decorated
@log_function_call
def say_hello():
    print("Hello, world!")

# Calling the decorated function
say_hello()

# 17. Class Decorators
# Assignment:17
# Create a class decorator add_greeting that modifies a class to add a greet() method returning
#  "Hello from Decorator!". Apply it to a class Person.

# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Applying the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Creating an instance of the decorated Person class
person = Person("Ali")

# Calling the greet method added by the decorator
print(person.greet())  # Output: Hello from Decorator!


# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:18
# Create a class Product with a private attribute _price.
#  Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        # Getter: returns the price
        return self._price

    @price.setter
    def price(self, value):
        # Setter: updates the price
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    @price.deleter
    def price(self):
        # Deleter: deletes the price
        print("Price has been deleted.")
        del self._price

# Example usage
product = Product(100)

# Accessing the price using the getter
print(f"Initial price: {product.price}")

# Updating the price using the setter
product.price = 150
print(f"Updated price: {product.price}")

# Trying to set a negative price
product.price = 50

# Deleting the price using the deleter
del product.price




# 19. callable() and __call__()
# Assignment:19
# Create a class Multiplier with an __init__() to set a factor. 
# Define a __call__() method that multiplies an input by the factor. 
# Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the multiplication factor

    def __call__(self, value):
        # Multiply the input by the factor
        return value * self.factor

# Create an object of Multiplier with a factor of 5
multiply_by_5 = Multiplier(5)

# Test if the object is callable
print(callable(multiply_by_5))  # Output: True

# Call the object like a function
result = multiply_by_5(10)  # The object is called with 10 as the input
print(f"Result of multiplying by 5: {result}")  # Output: 50


# 20. Creating a Custom Exception
# Assignment:20
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this 
# exception if age < 18. Handle it with try...except.

# Define a custom exception
class InvalidAgeError(Exception):
    pass

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older!")
    else:
        print("Age is valid.")

# Example usage with try-except
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter a valid number for age.")

# 21. Make a Custom Class Iterable
# Assignment:21
# Create a class Countdown that takes a start number.
#  Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.start = start  # Initialize the starting number
        self.current = start  # Set the current number to start

    def __iter__(self):
        # The object itself is the iterator, return the object
        return self

    def __next__(self):
        # If the current number is below 0, stop the iteration
        if self.current < 0:
            raise StopIteration
        # Otherwise, return the current number and decrease it by 1
        self.current -= 1
        return self.current + 1  # Return the current number before decrement

# Example usage: creating a Countdown object starting from 10
countdown = Countdown(10)

# Iterating through the Countdown object using a for loop
for number in countdown:
    print(number)
