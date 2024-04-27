import psycopg2

def postgres_connection():
    try:
        # Connecting to database
        # conn = psycopg2.connect(database = "adt_ride_share_database", 
        #         user = "postgres", 
        #         host= '127.0.0.1',
        #         password = "mz7zdz123",
        #         port = 5432)
        # Connecting to PostgreSQL hosted online
        conn = psycopg2.connect(database = "rideshare_hub", 
                user = "rideshare_hub_user", 
                host= 'dpg-com6i56n7f5s73d5ld4g-a.oregon-postgres.render.com',
                password = "nqvU0nhgNmQfiQfgP6LupSEoeIkgP5eE",
                port = 5432)

        print("PostgreSQL connection established")
        return conn
    except Exception as error:
        raise Exception("Error connecting to PostgreSQL database, error:{}".format(error))

## Creating tables and inserting few values
# Cursor to execute commands
conn = postgres_connection()
cur = conn.cursor()

# # SQL commands to create tables
# commands = [
#     """
#     CREATE TABLE Users(
#         user_id varchar(50), 
#         first_name varchar(50) NOT NULL,
#         last_name varchar(50) NOT NULL,
#         email_id varchar(50) NOT NULL,
#         contact varchar(15) NOT NULL,
#         user_password varchar(50) NOT NULL,
#         primary key (user_id)
#     );
#     """,
#     """
#     CREATE TABLE Cities(
#         city_id SERIAL,
#         city varchar(50) NOT NULL,
#         state varchar(50) NOT NULL,
#         country varchar(20) NOT NULL,
#         primary key (city_id)
#     );
#     """,
#     """
#     CREATE TABLE Currencies(
#         currency_id SERIAL,
#         currency varchar(10) NOT NULL,
#         primary key (currency_id)
#     );
#     """,
#     """
#     CREATE TABLE Rides(
#         ride_id SERIAL,
#         user_id varchar(50) NOT NULL,
#         departure_city_id int NOT NULL,
#         arrival_city_id int NOT NULL,
#         currency_id int NOT NULL,
#         departure_date date NOT NULL,
#         departure_time time NOT NULL,
#         arrival_date date NOT NULL,
#         arrival_time time NOT NULL,
#         vehicle_type varchar(50) NOT NULL,
#         vehicle_number varchar(20) NOT NULL,
#         vehicle_image bytea NULL,
#         pickup_loc varchar(100) NOT NULL,
#         dropoff_loc varchar(100) NOT NULL,
#         total_seats int NOT NULL,
#         reserved_seats int NOT NULL,
#         available_seats int NOT NULL,
#         price numeric NOT NULL,
#         special_amenities varchar(200) NULL,
#         active boolean NOT NULL,
#         primary key (ride_id),
#         foreign key (user_id) references Users(user_id) on delete cascade,
#         foreign key (departure_city_id) references Cities(city_id) on delete cascade,
#         foreign key (arrival_city_id) references Cities(city_id) on delete cascade,
#         foreign key (currency_id) references Currencies(currency_id) on delete cascade
#     );
#     """,
#     """
#     CREATE TABLE Bookings(
#         booking_id SERIAL,
#         ride_id int NOT NULL,
#         passenger_id varchar(50) NOT NULL,
#         number_of_seats_reserved int NOT NULL,
#         booking_date date NOT NULL,
#         booking_time time NOT NULL,
#         billed_amount numeric NOT NULL,
#         payment_status char(50) NULL,
#         primary key (booking_id),
#         foreign key (ride_id) references Rides(ride_id) on delete cascade,
#         foreign key (passenger_id) references Users(user_id) on delete cascade
#     );
#     """
# ]

# # Execute each command to create tables
# print("starting creating tables")
# for command in commands:
#     cur.execute(command)

# # Commit changes
# conn.commit()

# # Close communication with the PostgreSQL database server
# cur.close()
# conn.close()

# print("Tables created successfully!")

# inserting data
# SQL commands to insert data
commands = [
    """
    INSERT INTO Users (user_id, first_name, last_name, email_id, contact, user_password) 
    VALUES 
    ('1', 'Manikanta', 'Kodandapani', 'k11@iu.edu', '9301234567', 'password123'),
    ('2', 'Siddharth', 'Gosawi', 'sgosawi@iu.edu', '9401234567', 'abc123'),
    ('3', 'Monisha', 'Patro', 'monpatro@iu.edu', '9303331234', 'password@1234'),
    ('4', 'William', 'Wordsworth', 'daffodils@gmail.com', '9988776655', 'NEWPASSWORD'),
    ('5', 'Swarn', 'Gaba', 'sgaba@iu.edu', '8304567845', 'password');
    """,
    """
    INSERT INTO Cities (city, state, country) 
    VALUES 
    ('Chicago', 'IL', 'USA'),
    ('Indianapolis', 'IN', 'USA'),
    ('Bloomington', 'IN', 'USA'),
    ('Edinburgh', 'IN', 'USA'),
    ('Louisville', 'KY', 'USA');
    """,
    """
    INSERT INTO Currencies (currency) 
    VALUES 
    ('USD'),
    ('INR'),
    ('EUR'),
    ('GBP'),
    ('JPY'),
    ('CAD'),
    ('AUD'),
    ('CNY'),
    ('CHF'),
    ('RUB'),
    ('BRL');
    """,
    """
    INSERT INTO Rides (user_id, departure_city_id, arrival_city_id, currency_id, departure_date, departure_time, arrival_date, arrival_time, vehicle_type, vehicle_number, pickup_loc, dropoff_loc, total_seats, reserved_seats, available_seats, price, special_amenities, active) 
    VALUES 
    ('1', 3, 2, 1, '2024-04-07', '08:00', '2024-05-07', '09:00', 'SUV', 'ABC123', 'IMU', 'City Center', 6, 1, 5, 20.00, 'Wi-Fi', true),
    ('2', 2, 1, 2, '2024-04-08', '10:00', '2024-05-08', '13:00', 'Economy', 'DEF456', 'Railway Station', 'Trump Tower', 4, 0, 4, 10.00, 'AC', true),
    ('3', 1, 3, 1, '2024-04-09', '12:00', '2024-05-09', '16:00', 'Sedan', 'GHI789', 'Navy Pier', 'Luddy', 4, 0, 4, 15.00, NULL, true),
    ('4', 3, 1, 3, '2024-04-10', '14:00', '2024-05-10', '18:00', 'SUV', 'JKL012', 'McNutt', 'Airport', 6, 2, 4, 20.00, 'Child seat', true),
    ('5', 5, 2, 2, '2024-04-11', '16:00', '2024-05-11', '20:00', 'Economy', 'MNO345', 'KFC', 'Airport', 4, 1, 3, 10.00, 'Pet-friendly', true);
    """,
    """
    INSERT INTO Bookings (ride_id, passenger_id, number_of_seats_reserved, booking_date, booking_time, billed_amount, payment_status) 
    VALUES 
    (1, '2', 2, '2024-04-06', '15:30', 40.00, 'Booked'),  
    (1, '3', 3, '2024-04-06', '16:00', 60.00, 'Paid'),  
    (1, '4', 2, '2024-04-06', '15:30', 40.00, 'Booked'),  
    (1, '5', 3, '2024-04-06', '16:00', 60.00, 'Paid');
    """
]

# Execute each command to insert data
for command in commands:
    cur.execute(command)

# Commit changes
conn.commit()

# Close communication with the PostgreSQL database server
cur.close()
conn.close()

print("Data inserted successfully!")

