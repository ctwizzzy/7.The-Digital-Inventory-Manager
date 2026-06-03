class product: 
    def __init__(self, product_id, name, price, quantity):
     self.product_id = product_id
     self.name = name
     self.price = price
     self.quantity = quantity 

def add_stock(self, amount, quantity):
    self.amount = amount
    quantity = int(input("How much stock would you like to add?" ))
    amount = amount + quantity  
    

def remove_stock(self, amount, quantity):
    quantity = int(input("How much stock would you like to remove?" ))
    amount = amount - quantity 

def __str__(self): 
    return f"{self.product_id} | {self.name} | {self.price} | {self.quantity}"


class Inventory:   

def __init__(self, product):
    self.product = product


def get_total_value(self, price, amount):            
    value = amount * price
    return value      

def restock(self, product_id, amount):
    self.product_id = product_id
    if amount == 0:
        print("Out of stock, please restock")     

def display_all(self, product_id, name, price, amount):
    print("Product ID: ", product_id)
    print("Name: ", name)
    print("Price: ", price)
    print("Amount: ", amount) 


