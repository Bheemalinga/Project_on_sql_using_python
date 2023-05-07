import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Asdfghjkl123"
)

# Create a database named "Inventory_Management"
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Inventory_Management")











# Connect to the newly created database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Svbb@0808",
  database="Inventory_Management"
)

# Create the "manufacture" table
mycursor = mydb.cursor()
query = """CREATE TABLE manufacture (manufacture_id INT PRIMARY KEY, manufacture_name VARCHAR(200), product_name VARCHAR(200),quantity INT,
        defective_items INT,manufacturing_date DATE)"""
mycursor.execute(query)



# Create the "goods" table
query = """CREATE TABLE goods (goods_id INT PRIMARY KEY, product_name VARCHAR(200), quantity INT, manufacturing_date DATE,
        expiry_date DATE, price FLOAT)"""
mycursor.execute(query)



# Create the "purchase" table
query = """CREATE TABLE purchase (purchase_id INT AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(200), purchase_date DATE,
        purchase_amount FLOAT, Mode_of_purchase varchar(200), Defective_item_supplied VARCHAR(20), seller_name VARCHAR(200))"""
mycursor.execute(query)



# Create the "sale" table
query = """CREATE TABLE sale (sale_id INT PRIMARY KEY, product_name VARCHAR(200), sale_date DATE, sale_amount FLOAT,
        profit_margin FLOAT, store_name VARCHAR(200))"""
mycursor.execute(query)











# Insert sample data into the "manufacture" table
manufacture_data = [
  (1, "KK Export", "Glasses", 600, 30, "2022-01-01"),
  (2, "PVC Export", "Chairs", 800, 27,"2022-03-14"),
  (3, "SS Export", "Tables", 300, 9, "2022-03-21"),
  (4, "A-Z Export", "red-colored toys", 900, 150, "2022-05-27")
]
mycursor.executemany("INSERT INTO manufacture (manufacture_id, manufacture_name, product_name, quantity, defective_items, manufacturing_date) VALUES (%s, %s, %s, %s, %s, %s)", manufacture_data)
mydb.commit()



# Insert sample data into the "goods" table
goods_data = [
  (1, "wood", 1100, "2021-09-11", "2028-11-20", 2890.00),
  (2, "glue", 900, "2021-08-29", "2023-08-29", 3700.50),
  (3, "Screws", 1020, "2021-11-23", "2027-02-28", 1900.00),
  (4, "Plastic", 3000, "2021-01-07", "2026-04-07", 2000.00)
]
mycursor.executemany("INSERT INTO goods (goods_id , product_name , quantity , manufacturing_date , expiry_date , price ) VALUES (%s, %s, %s, %s, %s, %s)", goods_data)
mydb.commit()



# Insert sample data into the "purchase" table
purchase_data = [
  ("Glasses", "2023-01-30", 2500.00, "ONLINE", "YES", "T.Rahul"),
  ("Chairs", "2023-01-30",3000.00, "OFFLINE", "NO", "M.Mohit"),
  ("Tables", "2023-01-30",6500.00, "OFFLINE", "NO", "PV.Sindhu"),
  ("red-colored toys", "2023-01-30", 5000.00, "ONLINE", "NO", "A.Rohit")
]
mycursor.executemany("INSERT INTO purchase (product_name, purchase_date, purchase_amount, Mode_of_purchase, Defective_item_supplied, seller_name) VALUES (%s, %s, %s, %s, %s, %s)", purchase_data)
mydb.commit()



# Insert sample data into the "sale" table
sale_data = [
  (1, "Glasses", "2023-02-05", 19000.00, 5.7, "MyKids store"),
  (2, "Chairs", "2023-02-06", 16000.00, 8.6, "Srinivas store"),
  (3, "Tables", "2023-02-08", 12000.00, 3.2, "MyCare store"),
  (4, "red-colored toys", "2023-02-01", 10000.00, 10.0, "MyKids store")
]
mycursor.executemany("INSERT INTO sale (sale_id, product_name, sale_date, sale_amount, profit_margin, store_name) VALUES (%s, %s, %s, %s, %s, %s)", sale_data)
mydb.commit()
















'''   

Delete the Defective Items.

'''
mycursor = mydb.cursor()
sql_query = """ DELETE FROM PURCHASE WHERE Defective_item_supplied = "YES" """

mycursor.execute(sql_query)
mydb.commit()







"""

Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.

"""
mycursor = mydb.cursor()
sql_query = """ UPDATE manufacture JOIN purchase ON manufacture.product_name = purchase.product_name
SET manufacture.quantity = 450
WHERE manufacture.product_name = 'red-colored toys' AND purchase.seller_name = 'MyKids store' """

mycursor.execute(sql_query)
mydb.commit()







"""

Display all the “wooden chair” items that were manufactured before the 1st May 2023

"""
mycursor = mydb.cursor()
sql_query = """ SELECT product_name, quantity, defective_items, manufacturing_date FROM manufacture WHERE product_name = "Chairs" """

mycursor.execute(sql_query)
display = mycursor.fetchall()
for x in display:
    print(x)








"""

Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, manufactured by the “SS Export” company.

"""
mycursor = mydb.cursor()
sql_query = """ SELECT sale.profit_margin AS Profit_Margin FROM sale
JOIN manufacture ON sale.product_name = manufacture.product_name
WHERE sale.store_name = 'MyCare store' AND manufacture.manufacture_name = 'SS Export' AND sale.product_name = 'Tables';
 """

mycursor.execute(sql_query)
display = mycursor.fetchall()
for x in display:
    print(x)