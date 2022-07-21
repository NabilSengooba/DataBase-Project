from cs50 import SQL

import csv


open("sneakers.db", "w").close()

db = SQL("sqlite:///sneakers.db")



db.execute("CREATE TABLE customers(id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT);")

db.execute("CREATE TABLE Sneaker_brand(brand_name TEXT, price INT,sneaker_id INTEGER PRIMARY KEY AUTOINCREMENT);")

db.execute("CREATE TABLE Category(Cat_id INTEGER PRIMARY KEY AUTOINCREMENT,size TEXT,colour TEXT);")


db.execute("CREATE TABLE Cart_item(cart_id INTEGER PRIMARY KEY AUTOINCREMENT,quantity INT,total_cost INT);")


db.execute("CREATE TABLE Payment(payment_type TEXT,payment_id INTEGER PRIMARY KEY AUTOINCREMENT,total_cost INT);")

db.execute("CREATE TABLE Purchase_Details(pd_id INTEGER PRIMARY KEY AUTOINCREMENT,location TEXT,id INTEGER,sneaker_id INTEGER,Cat_id INTEGER ,cart_id INTEGER,payment_id INTEGER,FOREIGN KEY (id) REFERENCES customers(id),FOREIGN KEY (sneaker_id) REFERENCES Sneaker_brand(sneaker_id),FOREIGN KEY (Cat_id) REFERENCES Category(Cat_id),FOREIGN KEY(cart_id)  REFERENCES Cart_item(cart_id), FOREIGN KEY(payment_id) REFERENCES Payment(payment_id));")

  


with open("sneakers1.csv", "r")as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        
        emails = row["Email"]
        delivery_locations = row["Delivery Location"]
        phones= row["Phone number"]
        #names=row["Client"]
        sizes = row["Shoe Size"]
        prices = row["price"]
        colours = row["Shoe Colour"]
        brand_name= row["Brand name"]
        quatities= row["quantity"]
        #amounts= row["amount"]
        total_costs =row ["total cost"]
        payment_type= row["Payment type"]
        
        
        ids=db.execute("INSERT INTO customers(email) VALUES(?);",emails)
        cat= db.execute("INSERT INTO Category(size,colour) VALUES(?,?);",sizes,colours)
        sneak= db.execute("INSERT INTO Sneaker_brand(brand_name,price) VALUES(?,?);",brand_name,prices)
        cart=db.execute("INSERT INTO Cart_item(quantity,total_cost) VALUES(?,?);",quatities,total_costs)
        pay= db.execute("INSERT INTO Payment(payment_type,total_cost) VALUES(?,?);",payment_type,total_costs)
        
        db.execute("INSERT INTO purchase_details (location,id,sneaker_id,cat_id,cart_id,payment_id) VALUES(?,(SELECT id FROM customers WHERE  id = ?),(SELECT sneaker_id FROM Sneaker_brand WHERE sneaker_id = ?),(SELECT cat_id FROM Category WHERE cat_id = ?),(SELECT cart_id FROM Cart_item WHERE cart_id =?),(SELECT payment_id FROM Payment WHERE payment_id = ?));", delivery_locations,ids,sneak,cat,cart,pay)
