# Courier Management System

## TASK 1 Database Design

## TASK 1.1 ERD

![image](https://github.com/nandini-gangrade/Courier-Management-System/assets/87817417/52d13cb5-6529-44fb-9b0e-8a06253b3ab8)


## TASK 1.2 Relationship (Cardinality)

- **PARCEL -> ORDER (Many-to-One)**
  - Attributes: OrderID in the Parcels table is linked to OrderID in the Orders table.

- **ORDER -> CUSTOMER (Many-to-One)**
  - Attributes: CustomerID in the Orders table is linked to CustomerID in the Customers table.

- **ORDER -> COURIER (Many-to-One)**
  - Attributes: CourierID in the Orders table is linked to CourierID in the Couriers table.

- **COURIER -> USER (One-to-One)**
  - Attributes: UserID in the Couriers table is linked to UserID in the Users table.

- **COURIER -> PAYMENT (One-to-Many)**
  - Attributes: CourierID in the Payment table is linked to CourierID in the Couriers table.

- **COURIER -> COURIERSERVICEMAPPING (One-to-Many)**
  - Attributes: CourierID in the CourierServiceMapping table is linked to CourierID in the Couriers table.

- **COURIER -> EMPLOYEECOURIER (One-to-Many)**
  - Attributes: CourierID in the EmployeeCourier table is linked to CourierID in the Couriers table.

- **EMPLOYEE -> EMPLOYEECOURIER (One-to-Many)**
  - Attributes: EmployeeID in the EmployeeCourier table is linked to EmployeeID in the Employees table.

- **COURIERSERVICES -> COURIERSERVICEMAPPING (One-to-Many)**
  - Attributes: ServiceID in the CourierServiceMapping table is linked to ServiceID in the CourierServices table.

- **LOCATION -> PAYMENT (One-to-Many)**
  - Attributes: LocationID in the Payment table is linked to LocationID in the Location table.
<br>

## TASK 1.2 Insert Value Into The Table

### Create Tables

#### Users Table
```sql
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    Password VARCHAR(255),
    ContactNumber VARCHAR(20),
    Address TEXT
);
```

#### Customers Table
```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    ContactNumber VARCHAR(20),
    Address TEXT
);
```

#### Couriers Table
```sql
CREATE TABLE Couriers (
    CourierID INT PRIMARY KEY,
    UserID INT,
    SenderName VARCHAR(255),
    SenderAddress TEXT,
    ReceiverName VARCHAR(255),
    ReceiverAddress TEXT,
    Weight DECIMAL(5, 2),
    Status VARCHAR(50),
    TrackingNumber VARCHAR(20) UNIQUE,
    DeliveryDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
```

#### Orders Table
```sql
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    CourierID INT,
    OrderDate DATE,
    DeliveryDate DATE,
    Status VARCHAR(50),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (CourierID) REFERENCES Couriers(CourierID)
);
```

#### Parcels Table
```sql
CREATE TABLE Parcels (
    ParcelID INT PRIMARY KEY,
    OrderID INT,
    ParcelWeight DECIMAL(5, 2),
    ParcelDescription TEXT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
```

#### CourierServices Table
```sql
CREATE TABLE CourierServices (
    ServiceID INT PRIMARY KEY,
    ServiceName VARCHAR(100),
    Cost DECIMAL(8, 2)
);
```

#### Employee Table
```sql
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    ContactNumber VARCHAR(20),
    Role VARCHAR(50),
    Salary DECIMAL(10, 2)
);
```

#### Location Table
```sql
CREATE TABLE Location (
    LocationID INT PRIMARY KEY,
    LocationName VARCHAR(100),
    Address TEXT
);
```

#### Payment Table
```sql
CREATE TABLE Payment (
    PaymentID INT PRIMARY KEY,
    CourierID INT,
    LocationID INT,
    Amount DECIMAL(10, 2),
    PaymentDate DATE,
    FOREIGN KEY (CourierID) REFERENCES Couriers(CourierID),
    FOREIGN KEY (LocationID) REFERENCES Location(LocationID)
);
```

#### CourierServiceMapping Table
```sql
CREATE TABLE CourierServiceMapping (
    CourierID INT,
    ServiceID INT,
    FOREIGN KEY (CourierID) REFERENCES Couriers(CourierID),
    FOREIGN KEY (ServiceID) REFERENCES CourierServices(ServiceID)
);
```

#### EmployeeCourier Table
```sql
CREATE TABLE EmployeeCourier (
    EmployeeID INT,
    CourierID INT,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (CourierID) REFERENCES Couriers(CourierID)
);
```

### Insert Values

#### Customers Table
```sql
INSERT INTO Customers (CustomerID, Name, Email, ContactNumber, Address) VALUES
(1, 'John Doe', 'john@example.com', '1234567890', '123 Main Street'),
(2, 'Jane Smith', 'jane@example.com', '0987654321', '456 Elm Street'),
(3, 'Alice Johnson', 'alice@example.com', '9876543210', '789 Oak Street'),
(4, 'Bob Brown', 'bob@example.com', '5678901234', '101 Pine Street'),
(5, 'Emily Wilson', 'emily@example.com', '3456789012', '202 Maple Street'),
(6, 'David Lee', 'david@example.com', '4567890123', '303 Cedar Street'),
(7, 'Sarah Clark', 'sarah@example.com', '6543210987', '404 Birch Street');
```

#### Users Table
```sql
INSERT INTO Users (UserID, Name, Email, Password, ContactNumber, Address) VALUES
(101, 'John Smith', 'john.smith@example.com', 'password123', '1234567890', '123 Main Street'),
(102, 'Jane Doe', 'jane.doe@example.com', 'password456', '0987654321', '456 Elm Street'),
(103, 'Alice Johnson', 'alice.johnson@example.com', 'password789', '9876543210', '789 Oak Street'),
(104, 'Bob Brown', 'bob.brown@example.com', 'passwordabc', '5678901234', '101 Pine Street'),
(105, 'Emily Wilson', 'emily.wilson@example.com', 'passworddef', '3456789012', '202 Maple Street'),
(106, 'David Lee', 'david.lee@example.com', 'passwordghi', '4567890123', '303 Cedar Street'),
(107, 'Sarah Clark', 'sarah.clark@example.com', 'passwordjkl', '6543210987', '404 Birch Street');
```

#### Couriers Table
```sql
INSERT INTO Couriers (CourierID, UserID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate) VALUES
(201, 101, 'John Smith', '123 Main Street', 'Alice Johnson', '789 Oak Street', 2.5, 'In Transit', 'TN123456', '2024-05-05'),
(202, 102, 'Jane Doe', '456 Elm Street', 'Bob Brown', '101 Pine Street', 3.2, 'Delivered', 'TN654321', '2024-04-25'),
(203, 103, 'Alice Johnson', '789 Oak Street', 'Emily Wilson', '202 Maple Street', 1.8, 'Pending', 'TN987654', NULL),
(204, 104, 'Bob Brown', '101 Pine Street', 'David Lee', '303 Cedar Street', 4.7, 'In Transit', 'TN567890', NULL),
(205, 105, 'Emily Wilson', '202 Maple Street', 'Sarah Clark', '404 Birch Street', 3.9, 'Delivered', 'TN234567', '2024-04-30'),
(206, 106, 'David Lee', '303 Cedar Street', 'John Smith', '123 Main Street', 5.1, 'Pending', 'TN345678', NULL),
(207, 107, 'Sarah Clark', '404 Birch Street', 'Jane Doe', '456 Elm Street', 2.3, 'In Transit', 'TN456789', '2024-05-02');
```

#### CourierServices Table
```sql
INSERT INTO CourierServices (ServiceID, ServiceName, Cost) VALUES
(301, 'Standard', 10.00),
(302, 'Express', 20.00),
(303, 'Priority', 30.00),
(304, 'Premium', 40.00),
(305, 'Custom', 50.00),
(306, 'Superior', 60.00),
(307, 'Elite', 70.00);
```

#### Employee Table
```sql
INSERT INTO Employee (EmployeeID, Name, Email, ContactNumber, Role, Salary) VALUES
(401, 'Sarah Brown', 'sarah.brown@example.com', '1234567890', 'Manager', 5000.00),
(402, 'John Smith', 'john.smith@example.com', '9876543210', 'Courier', 3000.00),
(403, 'Alice Johnson', 'alice.johnson@example.com', '4567890123', 'Courier', 3000.00),
(404, 'Jane Doe', 'jane.doe@example.com', '2345678901', 'Courier', 3000.00),
(405, 'Bob Brown', 'bob.brown@example.com', '7890123456', 'Courier', 3000.00),
(406, 'Emily Wilson', 'emily.wilson@example.com', '8901234567', 'Courier', 3000.00),
(407, 'David Lee', 'david.lee@example.com', '3456789012', 'Courier', 3000.00);
```

#### Location Table
```sql
INSERT INTO Location (LocationID, LocationName, Address) VALUES
(701, 'Main Office', '123 Main Street'),
(702, 'Branch Office 1', '456 Elm Street'),
(703, 'Branch Office 2', '789 Oak Street'),
(704, 'Branch Office 3', '101 Pine Street'),
(705, 'Branch Office 4', '202 Maple Street'),
(706, 'Branch Office 5', '303 Cedar Street'),
(707, 'Branch Office 6', '404 Birch Street');
```

#### Payment Table
```sql
INSERT INTO Payment (PaymentID, CourierID, LocationID, Amount, PaymentDate) VALUES
(501, 201, 701, 40.00, '2024-04-25'),
(502, 202, 702, 50.00, '2024-04-27'),
(503, 203, 703, 60.00, '2024-04-29'),
(504, 204, 704, 70.00, '2024-05-01'),
(505, 205, 705, 80.00, '2024-05-03'),
(506, 206, 706, 30.00, '2024-05-05'),
(507, 207, 707, 45.00, '2024-05-07');
```

#### CourierServiceMapping Table
```sql
INSERT INTO CourierServiceMapping (CourierID, ServiceID) VALUES
(201, 301),
(202, 302),
(203, 303),
(204, 304),
(205, 305),
(206, 306),
(207, 307);
```

#### EmployeeCourier Table
```sql
INSERT INTO EmployeeCourier (EmployeeID, CourierID) VALUES
(402, 201),
(403, 202),
(404, 203),
(405, 204),
(406, 205),
(407, 206),
(401, 207);
```

#### Orders Table
```sql
INSERT INTO Orders (OrderID, CustomerID, CourierID, OrderDate, DeliveryDate, Status) VALUES
(301, 1, 201, '2024-04-20', '2024-04-25', 'Delivered'),
(302, 2, 202, '2024-04-22', '2024-04-27', 'Delivered'),
(303, 3, 203, '2024-04-24', NULL, 'Pending'),
(304, 4, 204, '2024-04-26', NULL, 'In Transit'),
(305, 5, 205, '2024-04-28', '2024-05-01', 'Delivered'),
(306, 6, 206, '2024-04-30', NULL, 'Pending'),
(307, 7, 207, '2024-05-02', '2024-05-05', 'In Transit');
```

#### Parcels Table
```sql
INSERT INTO Parcels (ParcelID, OrderID, ParcelWeight, ParcelDescription) VALUES
(401, 301, 2.5, 'Electronics'),
(402, 302, 3.2, 'Clothing'),
(403, 303, 1.8, 'Books'),
(404, 304, 4.7, 'Furniture'),
(405, 305, 3.9, 'Toys'),
(406, 306, 5.1, 'Appliances'),
(407, 307, 2.3, 'Jewelry');
```

### Generated Table

![image](https://github.com/nandini-gangrade/Courier-Management-System/assets/87817417/87b359db-2b27-4610-b21c-d4c395f40041)
![image](https://github.com/nandini-gangrade/Courier-Management-System/assets/87817417/7c79b65b-528a-445a-8511-3452ab403141)
![image](https://github.com/nandini-gangrade/Courier-Management-System/assets/87817417/45c949e9-7ef6-4a53-b59e-28ab15a3bbe2)

<br>

## TASK 2: Select, Where

### 1. List all customers
```sql
SELECT * FROM Customers;
```

### 2. List all orders for a specific customer ('John Doe')
```sql
SELECT * FROM Orders WHERE CustomerID = (SELECT CustomerID FROM Customers WHERE Name = 'John Doe');
```

### 3. List all couriers
```sql
SELECT * FROM Couriers;
```

### 4. List all packages for a specific order
```sql
SELECT * FROM Parcels WHERE OrderID = (SELECT OrderID FROM Orders WHERE Status = 'Delivered' AND CustomerID = (SELECT CustomerID FROM Customers WHERE Name = 'John Doe'));
```

### 5. List all deliveries for a specific courier
```sql
SELECT * FROM Orders WHERE CourierID = (SELECT CourierID FROM Couriers WHERE SenderName = 'John Smith');
```

### 6. List all undelivered packages
```sql
SELECT * FROM Parcels WHERE OrderID IN (SELECT OrderID FROM Orders WHERE Status = 'In Transit');
```

### 7. List all packages that are scheduled for delivery today
```sql
SELECT * FROM Orders WHERE DeliveryDate = CAST(GETDATE() AS DATE);
```

### 8. List all packages with a specific status
```sql
SELECT * FROM Orders WHERE Status = 'In Transit';
```

### 9. Calculate the total number of packages for each courier
```sql
SELECT CourierID, COUNT(*) AS TotalPackages FROM Orders GROUP BY CourierID;
```

### 10. Find the average delivery time for each courier
```sql
SELECT CourierID, AVG(DATEDIFF(day, OrderDate, DeliveryDate)) AS AvgDeliveryTime FROM Orders WHERE DeliveryDate IS NOT NULL GROUP BY CourierID;
```

### 11. List all packages with a specific weight range
```sql
SELECT * FROM Parcels WHERE ParcelWeight BETWEEN 3.0 AND 5.0;
```

### 12. Retrieve employees whose names contain 'John'
```sql
SELECT * FROM Employee WHERE Name LIKE '%John%';
```

### 13. Retrieve all courier records with payments greater than $50
```sql
SELECT * FROM Payment WHERE Amount > 50.00;
```
<br>

## TASK 3: GroupBy, Aggregate Functions, Having, Order By, where 

### 14. Find the total number of couriers handled by each employee
```sql
SELECT EmployeeCourier.EmployeeID, Employee.Name, COUNT(EmployeeCourier.CourierID) AS TotalCouriersHandled
FROM EmployeeCourier, Employee
WHERE EmployeeCourier.EmployeeID = Employee.EmployeeID
GROUP BY EmployeeCourier.EmployeeID, Employee.Name;
```

### 15. Calculate the total revenue generated by each location
```sql
SELECT Payment.LocationID, Location.LocationName, SUM(Payment.Amount) AS TotalRevenue
FROM Payment, Location
WHERE Payment.LocationID = Location.LocationID
GROUP BY Payment.LocationID, Location.LocationName;
```

### 16. Find the total number of couriers delivered to each location
```sql
SELECT Payment.LocationID, Location.LocationName, COUNT(DISTINCT Payment.CourierID) AS TotalCouriersDelivered
FROM Payment, Location
WHERE Payment.LocationID = Location.LocationID
GROUP BY Payment.LocationID, Location.LocationName;
```

### 17. Find the courier with the highest average delivery time
```sql
SELECT TOP 1 o.CourierID, AVG(DATEDIFF(day, o.OrderDate, o.DeliveryDate)) AS AvgDeliveryTime
FROM Orders o
WHERE o.DeliveryDate IS NOT NULL
GROUP BY o.CourierID
ORDER BY AvgDeliveryTime DESC;
```

### 18. Find Locations with Total Payments Less Than a Certain Amount
```sql
SELECT p.LocationID, SUM(p.Amount) AS TotalPayments
FROM Payment p
GROUP BY p.LocationID
HAVING SUM(p.Amount) < 5000;
```

### 19. Calculate Total Payments per Location
```sql
SELECT Payment.LocationID, Location.LocationName, SUM(Payment.Amount) AS TotalPayments
FROM Payment, Location
WHERE Payment.LocationID = Location.LocationID
GROUP BY Payment.LocationID, Location.LocationName;
```

### 20. Retrieve couriers who have received payments totaling more than $10 in a specific location (LocationID = X)
```sql
SELECT Couriers.*
FROM Couriers, (
    SELECT CourierID, SUM(Amount) AS TotalAmount
    FROM Payment
    WHERE LocationID = 701
    GROUP BY CourierID
    HAVING SUM(Amount) > 10
) AS Subquery
WHERE Couriers.CourierID = Subquery.CourierID;
```

### 21. Retrieve couriers who have received payments totaling more than $10 after a certain date (PaymentDate > 'YYYY-MM-DD')
```sql
SELECT Couriers.*
FROM Couriers, (
    SELECT CourierID, SUM(Amount) AS TotalAmount
    FROM Payment
    WHERE CONVERT(date, PaymentDate) > '2024-05-01' 
    GROUP BY CourierID
    HAVING SUM(Amount) > 10
) AS p
WHERE Couriers.CourierID = p.CourierID;
```

### 22. Retrieve locations where the total amount received is more than $50 before a certain date (PaymentDate > 'YYYY-MM-DD')
```sql
SELECT Location.*
FROM Location, (
    SELECT LocationID, SUM(Amount) AS TotalAmount
    FROM Payment
    WHERE PaymentDate > '2024-05-01'
    GROUP BY LocationID
    HAVING SUM(Amount) > 50
) AS Subquery
WHERE Location.LocationID = Subquery.LocationID;
```
<br>

## TASK 4: Inner Join, Full Outer Join, Cross Join, Left Outer Join, Right Outer Join

### 23. Retrieve Payments with Courier Information 
```sql
SELECT Payment.*, Couriers.*
FROM Payment
INNER JOIN Couriers ON Payment.CourierID = Couriers.CourierID;
```

### 24. Retrieve Payments with Location Information 
```sql
SELECT Payment.*, Location.*
FROM Payment
INNER JOIN Location ON Payment.LocationID = Location.LocationID;
```

### 25. Retrieve Payments with Courier and Location Information 
```sql
SELECT Payment.*, Couriers.*, Location.*
FROM Payment
INNER JOIN Couriers ON Payment.CourierID = Couriers.CourierID
INNER JOIN Location ON Payment.LocationID = Location.LocationID;
```

### 26. List all payments with courier details 
```sql
SELECT Payment.*, Couriers.*
FROM Payment
LEFT OUTER JOIN Couriers ON Payment.CourierID = Couriers.CourierID;
```

### 27. Total payments received for each courier 
```sql
SELECT Couriers.CourierID, SUM(Payment.Amount) AS TotalPayments
FROM Couriers
LEFT OUTER JOIN Payment ON Couriers.CourierID = Payment.CourierID
GROUP BY Couriers.CourierID;
```

### 28. List payments made on a specific date 
```sql
SELECT *
FROM Payment
WHERE PaymentDate = '2024-05-01'; 
```

### 29. Get Courier Information for Each Payment 
```sql
SELECT Payment.*, Couriers.*
FROM Payment
LEFT OUTER JOIN Couriers ON Payment.CourierID = Couriers.CourierID;
```

### 30. Get Payment Details with Location 
```sql
SELECT Payment.*, Location.*
FROM Payment
LEFT OUTER JOIN Location ON Payment.LocationID = Location.LocationID;
```

### 31. Calculating Total Payments for Each Courier 
```sql
SELECT Couriers.CourierID, SUM(Payment.Amount) AS TotalPayments
FROM Couriers
LEFT OUTER JOIN Payment ON Couriers.CourierID = Payment.CourierID
GROUP BY Couriers.CourierID;
```

### 32. List Payments Within a Date Range 
```sql
SELECT *
FROM Payment
WHERE PaymentDate BETWEEN '2024-04-25' AND '2024-05-03';
```

### 33. Retrieve a list of all users and their corresponding courier records, including cases where there are no matches on either side 
```sql
SELECT *
FROM Users
FULL OUTER JOIN Couriers ON Users.UserID = Couriers.UserID;
```

### 34. Retrieve a list of all couriers and their corresponding services, including cases where there are no matches on either side 
```sql
SELECT *
FROM Couriers
FULL OUTER JOIN Payment ON Couriers.CourierID = Payment.CourierID;
```

### 35. Retrieve a list of all employees and their corresponding payments, including cases where there are no matches on either side 
```sql
SELECT *
FROM Employee
FULL OUTER JOIN Payment ON Employee.EmployeeID = Payment.CourierID;
```

### 36. List all users and all courier services, showing all possible combinations. 
```sql
SELECT *
FROM Users
CROSS JOIN Couriers;
```

### 37. List all employees and all locations, showing all possible combinations: 
```sql
SELECT *
FROM Employee
CROSS JOIN Location;
```

### 38. Retrieve a list of couriers and their corresponding sender information (if available) 
```sql
SELECT *
FROM Couriers
LEFT OUTER JOIN Users AS Sender ON Couriers.UserID = Sender.UserID;
```

### 39. Retrieve a list of couriers and their corresponding receiver information (if available): 
```sql
SELECT *
FROM Couriers
LEFT OUTER JOIN Users AS Receiver ON Couriers.UserID = Receiver.UserID;
```

### 40. Retrieve a list of couriers along with the courier service details (if available): 
```sql
SELECT *
FROM Couriers
LEFT OUTER JOIN CourierServiceMapping ON Couriers.CourierID = CourierServiceMapping.CourierID
LEFT OUTER JOIN CourierServices ON CourierServiceMapping.ServiceID = CourierServices.ServiceID;
```

### 41. Retrieve a list of employees and the number of couriers assigned to each employee: 
```sql
SELECT Employee.EmployeeID, Employee.Name, COUNT(EmployeeCourier.CourierID) AS TotalCouriersAssigned
FROM Employee
LEFT OUTER JOIN EmployeeCourier ON Employee.EmployeeID = EmployeeCourier.EmployeeID
GROUP BY Employee.EmployeeID, Employee.Name;
```

### 42. Retrieve a list of locations and the total payment amount received at each location: 
```sql
SELECT Location.LocationID, Location.LocationName, SUM(Payment.Amount) AS TotalPaymentsReceived
FROM Location
LEFT OUTER JOIN Payment ON Location.LocationID = Payment.LocationID
GROUP BY Location.LocationID, Location.LocationName;
```

### 43. Retrieve all couriers sent by the same sender (based on SenderName). 
```sql
SELECT *
FROM Couriers AS c1
INNER JOIN Couriers AS c2 ON c1.SenderName = c2.SenderName AND c1.CourierID != c2.CourierID;
```

### 44. List all employees who share the same role. 
```sql
SELECT *
FROM Employee AS e1
INNER JOIN Employee AS e2 ON e1.Role = e2.Role AND e1.EmployeeID != e2.EmployeeID;
```

### 45. Retrieve all payments made for couriers sent from the same location. 
```sql
SELECT *
FROM Payment AS p1
INNER JOIN Payment AS p2 ON p1.LocationID = p2.LocationID AND p1.CourierID != p2.CourierID;
```

### 46. Retrieve all couriers sent from the same location (based on SenderAddress). 
```sql
SELECT *
FROM Couriers AS c1
INNER JOIN Couriers AS c2 ON c1.SenderAddress = c2.SenderAddress AND c1.CourierID != c2.CourierID;
```

### 47. List employees and the number of couriers they have delivered: 
```sql
SELECT Employee.EmployeeID, Employee.Name, COUNT(Orders.CourierID) AS TotalCouriersDelivered
FROM Employee
LEFT OUTER JOIN Orders ON Employee.EmployeeID = Orders.CourierID
GROUP BY Employee.EmployeeID, Employee.Name;
```

### 48. Find couriers that were paid an amount greater than the cost of their respective courier services
```sql
SELECT *
FROM Payment
INNER JOIN Couriers ON Payment.CourierID = Couriers.CourierID
INNER JOIN CourierServiceMapping ON Couriers.CourierID = CourierServiceMapping.CourierID
INNER JOIN CourierServices ON CourierServiceMapping.ServiceID = CourierServices.ServiceID
WHERE Payment.Amount > CourierServices.Cost;
```
<br>

## TASK 5: Scope - Inner Queries, Non Equi Joins, Equi joins,Exist,Any,All 

### 49. Find couriers that have a weight greater than the average weight of all couriers
```sql
SELECT *
FROM Couriers
WHERE Weight > (SELECT AVG(Weight) FROM Couriers);
```

### 50. Find the names of all employees who have a salary greater than the average salary
```sql
SELECT Name
FROM Employee
WHERE Salary > (SELECT AVG(Salary) FROM Employee);
```

### 51. Find the total cost of all courier services where the cost is less than the maximum cost
```sql
SELECT SUM(Cost) As TotalCost
FROM CourierServices
WHERE Cost < (SELECT MAX(Cost) FROM CourierServices);
```

### 52. Find all couriers that have been paid for
```sql
SELECT *
FROM Couriers
WHERE EXISTS (
    SELECT 1
    FROM Payment
    WHERE Payment.CourierID = Couriers.CourierID
);
```

### 53. Find the locations where the maximum payment amount was made
```sql
SELECT LocationID
FROM Payment
WHERE Amount = (SELECT MAX(Amount) FROM Payment);
```

### 54. Find all couriers whose weight is greater than the weight of all couriers sent by a specific sender
```sql
SELECT *
FROM Couriers AS c1
WHERE Weight > ALL (
    SELECT Weight
    FROM Couriers AS c2
    WHERE c2.SenderName = 'Alice Johnson'
);
```
