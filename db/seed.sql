
-- Data Insertion Queries

INSERT INTO Customer (CustomerID, Name, Email, ContactNumber, Address) VALUES
(1, 'John Doe', 'john@example.com', '1234567890', '123 Main Street'),
(2, 'Jane Smith', 'jane@example.com', '0987654321', '456 Elm Street'),
(3, 'Alice Johnson', 'alice@example.com', '9876543210', '789 Oak Street'),
(4, 'Bob Brown', 'bob@example.com', '5678901234', '101 Pine Street'),
(5, 'Emily Wilson', 'emily@example.com', '3456789012', '202 Maple Street'),
(6, 'David Lee', 'david@example.com', '4567890123', '303 Cedar Street'),
(7, 'Sarah Clark', 'sarah@example.com', '6543210987', '404 Birch Street');

INSERT INTO Users (UserID, Name, Email, Password, ContactNumber, Address) VALUES
(101, 'John Smith', 'john.smith@example.com', 'password123', '1234567890', '123 Main Street'),
(102, 'Jane Doe', 'jane.doe@example.com', 'password456', '0987654321', '456 Elm Street'),
(103, 'Alice Johnson', 'alice.johnson@example.com', 'password789', '9876543210', '789 Oak Street'),
(104, 'Bob Brown', 'bob.brown@example.com', 'passwordabc', '5678901234', '101 Pine Street'),
(105, 'Emily Wilson', 'emily.wilson@example.com', 'passworddef', '3456789012', '202 Maple Street'),
(106, 'David Lee', 'david.lee@example.com', 'passwordghi', '4567890123', '303 Cedar Street'),
(107, 'Sarah Clark', 'sarah.clark@example.com', 'passwordjkl', '6543210987', '404 Birch Street');

INSERT INTO Courier (CourierID, UserID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate) VALUES
(201, 101, 'John Smith', '123 Main Street', 'Alice Johnson', '789 Oak Street', 2.5, 'In Transit', 'TN123456', '2024-05-05'),
(202, 102, 'Jane Doe', '456 Elm Street', 'Bob Brown', '101 Pine Street', 3.2, 'Delivered', 'TN654321', '2024-04-25'),
(203, 103, 'Alice Johnson', '789 Oak Street', 'Emily Wilson', '202 Maple Street', 1.8, 'Pending', 'TN987654', NULL),
(204, 104, 'Bob Brown', '101 Pine Street', 'David Lee', '303 Cedar Street', 4.7, 'In Transit', 'TN567890', NULL),
(205, 105, 'Emily Wilson', '202 Maple Street', 'Sarah Clark', '404 Birch Street', 3.9, 'Delivered', 'TN234567', '2024-04-30'),
(206, 106, 'David Lee', '303 Cedar Street', 'John Smith', '123 Main Street', 5.1, 'Pending', 'TN345678', NULL),
(207, 107, 'Sarah Clark', '404 Birch Street', 'Jane Doe', '456 Elm Street', 2.3, 'In Transit', 'TN456789', '2024-05-02');

INSERT INTO CourierServices (ServiceID, ServiceName, Cost) VALUES
(301, 'Standard', 10.00),
(302, 'Express', 20.00),
(303, 'Priority', 30.00),
(304, 'Premium', 40.00),
(305, 'Custom', 50.00),
(306, 'Superior', 60.00),
(307, 'Elite', 70.00);

INSERT INTO Employee (EmployeeID, Name, Email, ContactNumber, Role, Salary) VALUES
(401, 'Sarah Brown', 'sarah.brown@example.com', '1234567890', 'Manager', 5000.00),
(402, 'John Smith', 'john.smith@example.com', '9876543210', 'Courier', 3000.00),
(403, 'Alice Johnson', 'alice.johnson@example.com', '4567890123', 'Courier', 3000.00),
(404, 'Jane Doe', 'jane.doe@example.com', '2345678901', 'Courier', 3000.00),
(405, 'Bob Brown', 'bob.brown@example.com', '7890123456', 'Courier', 3000.00),
(406, 'Emily Wilson', 'emily.wilson@example.com', '8901234567', 'Courier', 3000.00),
(407, 'David Lee', 'david.lee@example.com', '3456789012', 'Courier', 3000.00);

INSERT INTO Location (LocationID, LocationName, Address) VALUES
(701, 'Main Office', '123 Main Street'),
(702, 'Branch Office 1', '456 Elm Street'),
(703, 'Branch Office 2', '789 Oak Street'),
(704, 'Branch Office 3', '101 Pine Street'),
(705, 'Branch Office 4', '202 Maple Street'),
(706, 'Branch Office 5', '303 Cedar Street'),
(707, 'Branch Office 6', '404 Birch Street');

INSERT INTO Payment (PaymentID, CourierID, LocationID, Amount, PaymentDate) VALUES
(501, 201, 701, 40.00, '2024-04-25'),
(502, 202, 702, 50.00, '2024-04-27'),
(503, 203, 703, 60.00, '2024-04-29'),
(504, 204, 704, 70.00, '2024-05-01'),
(505, 205, 705, 80.00, '2024-05-03'),
(506, 206, 706, 30.00, '2024-05-05'),
(507, 207, 707, 45.00, '2024-05-07');

INSERT INTO CourierServiceMapping (CourierID, ServiceID) VALUES
(201, 301),
(202, 302),
(203, 303),
(204, 304),
(205, 305),
(206, 306),
(207, 307);

INSERT INTO EmployeeCourier (EmployeeID, CourierID) VALUES
(402, 201),
(403, 202),
(404, 203),
(405, 204),
(406, 205),
(407, 206),
(401, 207);

INSERT INTO [Order] (OrderID, CustomerID, CourierID, OrderDate, DeliveryDate, Status) VALUES
(301, 1, 201, '2024-04-20', '2024-04-25', 'Delivered'),
(302, 2, 202, '2024-04-22', '2024-04-27', 'Delivered'),
(303, 3, 203, '2024-04-24', NULL, 'Pending'),
(304, 4, 204, '2024-04-26', NULL, 'In Transit'),
(305, 5, 205, '2024-04-28', '2024-05-01', 'Delivered'),
(306, 6, 206, '2024-04-30', NULL, 'Pending'),
(307, 7, 207, '2024-05-02', '2024-05-05', 'In Transit');

INSERT INTO Parcel (ParcelID, OrderID, ParcelWeight, ParcelDescription) VALUES
(401, 301, 2.5, 'Electronics'),
(402, 302, 3.2, 'Clothing'),
(403, 303, 1.8, 'Books'),
(404, 304, 4.7, 'Furniture'),
(405, 305, 3.9, 'Toys'),
(406, 306, 5.1, 'Appliances'),
(407, 307, 2.3, 'Jewelry');

