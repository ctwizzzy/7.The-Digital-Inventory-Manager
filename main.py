class product: 
    def __init__(self, product_id, name, price, quantity):
     self.product_id = product_id
     self.name = name
     self.price = price
     self.quantity = quantity 

def add_stock(self, amount):
    self.amount = amount
    return amount + 1
    

def remove_stock(self, amount):

    if amount == -1:
        print("Unavailable, stock cannot be negative")

   
       
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

class Inventory:
    def __init__(self): 
        self.products = {}    

def add_product(self, product):
    self.products = product{product.product_id} = product

def restock(self, product_id, amount):
    self.product_id = product_id
    if amount == 0:
        print("Out of stock, please restock")  
    