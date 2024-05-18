# Task 1: Control Flow Statements
## 1. Check Delivery Status:
**- Write a Python function to check whether a given order is delivered or not based on its status.**

```python
def check_delivery_status(status):
    if status.lower() == "delivered":
        return True
    else:
        return False

# Example usage:
status = "Delivered"
is_delivered = check_delivery_status(status)
print(f"Is the order delivered? {is_delivered}")
```

## 2. Categorize Parcels by Weight:
**- Implement a switch-case statement to categorize parcels based on their weight into "Light," "Medium," or "Heavy."**

```python
def categorize_parcel(weight):
    if weight < 2:
        category = "Light"
    elif 2 <= weight <= 5:
        category = "Medium"
    else:
        category = "Heavy"
    return category

# Example usage:
weight = 3.5
parcel_category = categorize_parcel(weight)
print(f"The parcel is categorized as {parcel_category}.")
```

## 3. User Authentication:
**- Create a login system for employees and customers using Python control flow statements.**

```python
def login(username, password):
    # Dummy authentication logic, replace with actual authentication logic
    if username == "admin" and password == "password":
        return True
    else:
        return False

# Example usage:
username = input("Enter username: ")
password = input("Enter password: ")
if login(username, password):
    print("Login successful!")
else:
    print("Invalid username or password.")
```

## 4. Courier Assignment Logic:
**- Develop a mechanism to assign couriers to shipments based on predefined criteria (e.g., proximity, load capacity) using loops.**

```python
def assign_courier(order, couriers):
    for courier in couriers:
        # Implement your criteria for assigning courier to order
        # For example, check proximity, load capacity, availability, etc.
        if courier.is_available() and courier.has_capacity(order.weight):
            courier.assign_order(order)
            return courier
    return None  # No available courier found

# Example usage:
assigned_courier = assign_courier(order, available_couriers)
if assigned_courier:
    print(f"Order assigned to courier {assigned_courier.name}.")
else:
    print("No available courier found for the order.")
```
---

# Task 2: Loops and Iteration
## 5. Display Orders for a Specific Customer:
**- Write a Python program that uses a loop to display all the orders for a specific customer.**

```python
# Assuming you have a function to retrieve orders for a specific customer from the database
def get_orders_for_customer(customer_id):
    # Retrieve orders from database based on customer_id
    orders = []  # Replace this with actual database query
    return orders

# Example usage:
customer_id = 1
orders = get_orders_for_customer(customer_id)
print("Orders for Customer:")
for order in orders:
    print(order)  # Display order details
```

## 6. Track Courier's Real-Time Location:
**- Implement a while loop to track the real-time location of a courier until it reaches its destination.**

```python
# Assuming you have a function to get real-time location updates for a courier
def track_courier(courier_id):
    # Track courier's location until destination is reached
    while not destination_reached(courier_id):
        location = get_courier_location(courier_id)
        print(f"Courier's current location: {location}")
        # Add logic to pause for some time before getting the next location update

# Example usage:
courier_id = 201
track_courier(courier_id)
```
---
# Task 3: Arrays and Data Structures
## 7. Tracking History of a Parcel:
**- Create an array to store the tracking history of a parcel, where each entry represents a location update.**

```python
# Assuming you have a Parcel class with a tracking_history attribute
class Parcel:
    def __init__(self, tracking_number):
        self.tracking_number = tracking_number
        self.tracking_history = []

# Example usage:
parcel1 = Parcel("TN123456")
parcel1.tracking_history.append("Location 1: In transit")
parcel1.tracking_history.append("Location 2: Out for delivery")
print("Tracking history of Parcel 1:", parcel1.tracking_history)
```

## 8. Find Nearest Available Courier:
**- Implement a method to find the nearest available courier for a new order using an array of couriers.**

```python
def find_nearest_available_courier(customer_location, couriers):
    available_couriers = [courier for courier in couriers if courier.is_available()]
    if not available_couriers:
        return None

    # Calculate distances from customer location to each available courier
    distances = {}
    for courier in available_couriers:
        distance = calculate_distance(customer_location, courier.current_location)
        distances[courier] = distance

    # Sort couriers by distance and return nearest one
    nearest_courier = min(distances, key=distances.get)
    return nearest_courier

# Example usage:
customer_location = "New York, NY"
nearest_courier = find_nearest_available_courier(customer_location, couriers)
if nearest_courier:
    print(f"The nearest available courier is {nearest_courier.name}.")
else:
    print("No available couriers found.")

```
---

# Task 4: Strings, 2D Arrays, User-defined Functions, Hashmap
## 9. Parcel Tracking:
**- Create a program that allows users to input a parcel tracking number. Store the tracking number and status in a 2D String Array. Simulate the tracking process by displaying messages based on the tracking number's status.**

```python
# Assuming you have a dictionary or database to store parcel tracking information
parcel_tracking = {
    "TN123456": "In transit",
    "TN654321": "Out for delivery",
    # Add more tracking numbers and statuses as needed
}

def track_parcel(tracking_number):
    if tracking_number in parcel_tracking:
        status = parcel_tracking[tracking_number]
        print(f"Parcel with tracking number {tracking_number} is {status}.")
    else:
        print("Tracking number not found.")

# Example usage:
track_number = input("Enter parcel tracking number: ")
track_parcel(track_number)
```

## 10. Customer Data Validation:
**- Write a function to validate customer information such as name, address, and phone number based on specified criteria.**

```python
import re

def validate_customer_info(data, detail):
    if detail.lower() == "name":
        # Name should contain only letters and properly capitalized
        if re.match("^[A-Za-z ]+$", data):
            return True
        else:
            return False
    elif detail.lower() == "address":
        # Address should not contain special characters
        if re.match("^[A-Za-z0-9\s,'-]*$", data):
            return True
        else:
            return False
    elif detail.lower() == "phone":
        # Phone number should follow specific format (e.g., ###-###-####)
        if re.match("^\d{3}-\d{3}-\d{4}$", data):
            return True
        else:
            return False
    else:
        return False  # Invalid detail provided

# Example usage:
name = "John Doe"
is_valid_name = validate_customer_info(name, "name")
print(f"Is the name valid? {is_valid_name}")
```

## 11. Address Formatting:
**- Develop a function that takes an address as input and formats it correctly.**

```python
def format_address(address):
    # Capitalize the first letter of each word
    formatted_address = ' '.join(word.capitalize() for word in address.split())
    return formatted_address

# Example usage:
address = "123 main street, new york, ny 10001"
formatted_address = format_address(address)
print("Formatted address:", formatted_address)
```

## 12. Order Confirmation Email:
**- Create a program that generates an order confirmation email with details such as the customer's name, order number, delivery address, and expected delivery date.**

```python
def generate_order_confirmation_email(order_number, customer_name, delivery_address, delivery_date):
    email_content = f"Dear {customer_name},\n\nYour order with order number {order_number} has been confirmed.\nDelivery Address: {delivery_address}\nExpected Delivery Date: {delivery_date}\n\nThank you for choosing our service!"
    return email_content

# Example usage:
order_number = "ORD123456"
customer_name = "John Doe"
delivery_address = "123 Main Street, New York, NY"
delivery_date = "2024-05-25"
confirmation_email = generate_order_confirmation_email(order_number, customer_name, delivery_address, delivery_date)
print("Order confirmation email:")
print(confirmation_email)
```

## 13. Calculate Shipping Costs:
**- Develop a function that calculates the shipping cost based on the distance between two locations and the weight of the parcel.**

```python
def calculate_shipping_cost(source, destination, parcel_weight):
    # Dummy calculation, replace with actual logic based on your business requirements
    distance = 100  # Example distance between source and destination in miles
    cost_per_mile = 0.5  # Example cost per mile
    shipping_cost = distance * cost_per_mile * parcel_weight
    return shipping_cost

# Example usage:
source_address = "New York, NY"
destination_address = "Los Angeles, CA"
parcel_weight = 5.0  # in pounds
shipping_cost = calculate_shipping_cost(source_address, destination_address, parcel_weight)
print("Shipping cost:", shipping_cost)
```

## 14. Password Generator:
**- Create a function that generates secure passwords for courier system accounts.**

```python
import random
import string

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(random.choice(characters) for _ in range(length))
    return secure_password

# Example usage:
password = generate_password()
print("Generated password:", password)
```

## 15. Find Similar Addresses:
**- Implement a function that finds similar addresses in the system using string functions.**

```python
def find_similar_addresses(address, address_list):
    similar_addresses = []
    for addr in address_list:
        if address.lower() in addr.lower() or addr.lower() in address.lower():
            similar_addresses.append(addr)
    return similar_addresses

# Example usage:
address_to_check = "123 Main St, New York, NY"
address_list = ["123 Main St, New York, NY", "456 Elm St, Los Angeles, CA", "789 Oak St, Chicago, IL"]
similar_addresses = find_similar_addresses(address_to_check, address_list)
print("Similar addresses:", similar_addresses)
```

