# Problem 1: Bank Account Create a class representing a bank account with attributes like account number,
# account holder name, and balance. Implement methods to deposit and withdraw money from the account.

# class BankAccount:
#     def __init__(self, account_number, account_holder_name, balance=0.0):
#         self.account_number = account_number
#         self.account_holder_name = account_holder_name
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
#         else:
#             print("Invalid deposit amount. Please deposit a positive amount.")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
#         else:
#             print("Invalid withdrawal amount or insufficient funds.")
#
#     def __str__(self):
#         return f"Account Holder: {self.account_holder_name}\nAccount Number: {self.account_number}\nBalance: ₹{self.balance}"
#
# my_account = BankAccount(account_number="123456789", account_holder_name="Avinash Rai")
#
# # Depositing and withdrawing money
# my_account.deposit(1000)
# my_account.withdraw(500)
#
# # Displaying account information
# print("\nAccount Information:")
# print(my_account)

# Problem 2: Employee Management Create a class representing an employee with attributes like employee ID, name, and salary.
# Implement methods to calculate the yearly bonus and display employee details.

# class EmployeeManagement:
#
#     def __init__(self, employee_name, employee_id, employee_salary):
#         self.employee_name = employee_name
#         self.employee_id = employee_id
#         self.employee_salary = employee_salary
#
#     def get_employee_name(self):
#         return self.employee_name
#
#     def get_employee_id(self):
#         return self.employee_id
#
#     def get_employee_salary(self):
#         return self.employee_salary
#
#     def get_yearly_bonus(self):
#         return int(self.employee_salary*.90) # assuming the yearly bonus is 90 % of employee salary
#
# # Usage
# employee1 = EmployeeManagement(employee_name="Avinash Rai", employee_id=13123, employee_salary=5000000)
# print("Employee details\n")
# print(f"Employee Name: {employee1.get_employee_name()}"
#       f"\nEmployee ID: {employee1.get_employee_id()}"
#       f"\nEmployee Salary: ₹{employee1.get_employee_salary()} per year"
#       f"\nEmployee Bonus: ₹{employee1.get_yearly_bonus()} per year")


# "Problem 3: Vehicle Rental Create a class representing a vehicle rental system.
# Implement methods to rent a vehicle, return a vehicle, and display available vehicles.
# class VehicleRentalSystem:
#     def __init__(self):
#         self.available_vehicles = {}
#
#     def add_vehicle(self, vehicle_id, vehicle_type):
#         if vehicle_id not in self.available_vehicles:
#             self.available_vehicles[vehicle_id] = vehicle_type
#             print(f"Vehicle {vehicle_id} ({vehicle_type}) added to the rental system.")
#         else:
#             print(f"Vehicle {vehicle_id} is already in the rental system.")
#
#     def rent_vehicle(self, vehicle_id):
#         if vehicle_id in self.available_vehicles:
#             vehicle_type = self.available_vehicles.pop(vehicle_id)
#             print(f"Vehicle {vehicle_id} ({vehicle_type}) rented successfully.")
#         else:
#             print(f"Vehicle {vehicle_id} is not available for rent.")
#
#     def return_vehicle(self, vehicle_id, vehicle_type):
#         if vehicle_id not in self.available_vehicles:
#             self.available_vehicles[vehicle_id] = vehicle_type
#             print(f"Vehicle {vehicle_id} ({vehicle_type}) returned successfully.")
#         else:
#             print(f"Vehicle {vehicle_id} is already available in the rental system.")
#
#     def display_available_vehicles(self):
#         if not self.available_vehicles:
#             print("No vehicles available for rent.")
#         else:
#             print("Available Vehicles:",self.available_vehicles)
#             for vehicle_id, vehicle_type in self.available_vehicles.items():
#                 print(f"  {vehicle_id}: {vehicle_type}")
#
#
# # Usage
# rental_system = VehicleRentalSystem()
#
# # Adding vehicles to the system
# rental_system.add_vehicle(vehicle_id="001", vehicle_type="Sedan")
# rental_system.add_vehicle(vehicle_id="002", vehicle_type="SUV")
# rental_system.add_vehicle(vehicle_id="003", vehicle_type="Compact")
#
# # Displaying available vehicles
# rental_system.display_available_vehicles()
#
# # Renting a vehicle
# rental_system.rent_vehicle(vehicle_id="001")
#
# # Displaying available vehicles after renting
# rental_system.display_available_vehicles()
#
# # Returning a vehicle
# rental_system.return_vehicle(vehicle_id="001", vehicle_type="Sedan")
#
# # Displaying available vehicles after returning
# rental_system.display_available_vehicles()


# Problem 4: Library Catalog Create classes representing a library and a book.
# Implement methods to add books to the library, borrow books, and display available books.
# class Book:
#     def __init__(self, book_id, title, author):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.is_borrowed = False
#
#     def borrow(self):
#         if not self.is_borrowed:
#             self.is_borrowed = True
#             return f"Book '{self.title}' by {self.author} has been borrowed."
#         else:
#             return f"Sorry, the book '{self.title}' is already borrowed."
#
#     def return_book(self):
#         if self.is_borrowed:
#             self.is_borrowed = False
#             return f"Book '{self.title}' by {self.author} has been returned."
#         else:
#             return f"This book is not currently borrowed."
#
#     def __str__(self):
#         return f"{self.title} by {self.author}"
#
#
# class Library:
#     def __init__(self):
#         self.books = {}
#
#     def add_book(self, book):
#         if book.book_id not in self.books:
#             self.books[book.book_id] = book
#             print(f"Book '{book.title}' added to the library.")
#         else:
#             print(f"Book '{book.title}' is already in the library.")
#
#     def borrow_book(self, book_id):
#         if book_id in self.books:
#             return self.books[book_id].borrow()
#         else:
#             return "Book not found in the library."
#
#     def return_book(self, book_id):
#         if book_id in self.books:
#             return self.books[book_id].return_book()
#         else:
#             return "Book not found in the library."
#
#     def display_available_books(self):
#         if not self.books:
#             print("No books available in the library.")
#         else:
#             print("Available Books:")
#             for book_id, book in self.books.items():
#                 if not book.is_borrowed:
#                     print(f"  {book_id}: {str(book)}")
#
#
# # usage:
#
# # Creating books
# book1 = Book(book_id="001", title="The Great Gatsby", author="F. Scott Fitzgerald")
# book2 = Book(book_id="002", title="To Kill a Mockingbird", author="Harper Lee")
# book3 = Book(book_id="003", title="1984", author="George Orwell")
#
# # Creating a library
# library = Library()
#
# # Adding books to the library
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
#
# # Displaying available books
# library.display_available_books()
#
# # Borrowing a book
# print(library.borrow_book("001"))
#
# # Displaying available books after borrowing
# library.display_available_books()
#
# # Returning a book
# print(library.return_book("001"))
#
# # Displaying available books after returning
# library.display_available_books()


# Problem 5: Product Inventory Create classes representing a product and an inventory system.
# Implement methods to add products to the inventory, update product quantity, and display available products.
# class Product:
#     def __init__(self, product_id, name, price, quantity):
#         self.product_id = product_id
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def update_quantity(self, new_quantity):
#         self.quantity = new_quantity
#
#     def __str__(self):
#         return f"{self.name} (ID: {self.product_id}) - ₹{self.price:.2f}, Quantity: {self.quantity}"
#
#
# class InventorySystem:
#     def __init__(self):
#         self.products = {}
#
#     def add_product(self, product):
#         if product.product_id not in self.products:
#             self.products[product.product_id] = product
#             print(f"Product '{product.name}' added to the inventory.")
#         else:
#             print(f"Product '{product.name}' is already in the inventory.")
#
#     def update_quantity(self, product_id, new_quantity):
#         if product_id in self.products:
#             self.products[product_id].update_quantity(new_quantity)
#             print(f"Quantity for product '{self.products[product_id].name}' updated to {new_quantity}.")
#         else:
#             print("Product not found in the inventory.")
#
#     def display_available_products(self):
#         if not self.products:
#             print("No products available in the inventory.")
#         else:
#             print("Available Products:")
#             for product_id, product in self.products.items():
#                 print(f"  {product_id}: {str(product)}")
#
#
# #  usage:
#
# # Creating products
# product1 = Product(product_id="001", name="Laptop", price=999.99, quantity=10)
# product2 = Product(product_id="002", name="Smartphone", price=499.99, quantity=20)
# product3 = Product(product_id="003", name="Headphones", price=79.99, quantity=30)
#
# # Creating an inventory system
# inventory_system = InventorySystem()
#
# # Adding products to the inventory
# inventory_system.add_product(product1)
# inventory_system.add_product(product2)
# inventory_system.add_product(product3)
#
# # Displaying available products
# inventory_system.display_available_products()
#
# # Updating product quantity
# inventory_system.update_quantity(product_id="001", new_quantity=8)
#
# # Displaying available products after updating quantity
# inventory_system.display_available_products()
