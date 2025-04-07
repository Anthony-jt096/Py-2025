#Ex-1
'''
def alarm_system():
    print("Enter command: 'alarm', 'maintenance', or 'exit'")
    
    passwrd = "1234"
    
    while True:
        
        usr_input = input("Enter a command: ").strip().lower()
        
        if usr_input == "alarm":
            print("[Alarm system initiated]")
        
        elif usr_input == "maintenance":
            
            entered_pass = input("Enter password: ").strip()
            if entered_pass == passwrd:  
                print("[Maintenance mode initiated]")
            else:
                print("[Incorrect password]")
        
        elif usr_input == "exit":
            print("[Exiting console...]")
            break
        
        else:
            print("[Invalid command]")

alarm_system()
'''

#Ex-2   .
'''
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price})"


class Inventory:
    def __init__(self):
        self.products = {}
    
    def add_product(self, product, quantity):
        if product.name in self.products:
            self.products[product.name] += quantity/
        else:
            self.products[product.name] = quantity
    
    def remove_product(self, product_name, quantity):
        if product_name not in self.products:
            print(f"Error: {product_name} not found!")
            return
        
        if self.products[product_name] < quantity:
            print(f"Error: not enough {product_name} in stock!")
            return
        
        self.products[product_name] -= quantity
        if self.products[product_name] == 0:
            del self.products[product_name]
    
    def check_stock(self, product_name):
        return self.products.get(product_name, 0)
    
    def __str__(self):
        return "\n".join(
            f"{name}: {quantity}"
            for name, quantity in self.products.items()
        )


# order processing
def create_order(inventory, items):  # items = {"product_name": quantity}
    for item, quantity in items.items():
        if inventory.check_stock(item) < quantity:
            print(f"Cannot process order: Not enough {item}")
            return False
'''

#Ex-3 -- 7 (concepts)
'''
class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        
    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        
    def add_comment(self, user, text):
        self.comments.append(Comment(user, text))

class Comment:
    def __init__(self, author, text):
        self.author = author
        self.text = text

# Usage
alice = User("Alice")
post = alice.create_post("Beautiful day!")
post.add_comment(User("Bob"), "Indeed!")

--------

class Animal:
    def __init__(self, species):
        self.species = species
        self.health = 100
        
    def eat(self, food):
        self.health += food.nutrition
        food.die()

class Plant:
    def __init__(self):
        self.alive = True
        self.nutrition = 20
        
    def die(self):
        self.alive = False

class Environment:
    def __init__(self):
        self.plants = [Plant() for _ in range(10)]
        self.animals = [Animal("Rabbit"), Animal("Fox")]
        
    def simulate_day(self):
        for animal in self.animals:
            if animal.health > 0 and self.plants:
                animal.eat(self.plants.pop())

                
--------
import csv

class CSVParser:
    def __init__(self, filename):
        self.data = []
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.data.append(row)
    
    def search(self, column, value):
        return [row for row in self.data if row.get(column) == value]
    
    def add_row(self, row):
        self.data.append(row)

# Usage
parser = CSVParser("data.csv")
print(parser.search("age", "25"))


--------

class Resource:
    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount

class Building:
    def __init__(self, type):
        self.type = type
        self.workers = []
        
class City:
    def __init__(self):
        self.resources = {"wood": 100, "stone": 50}
        self.buildings = []
        
    def construct_building(self, type, cost):
        if all(self.resources[r] >= cost[r] for r in cost):
            self.buildings.append(Building(type))
            for r in cost:
                self.resources[r] -= cost[r]

# Usage
metro = City()
metro.construct_building("House", {"wood": 20})

---------

import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        
    def fetch_users(self):
        response = requests.get(f"{self.base_url}/users")
        return [self._format_user(u) for u in response.json()]
    
    def _format_user(self, data):
        return f"{data['name']} ({data['email']})"

# Usage
client = APIClient("https://jsonplaceholder.typicode.com")
print(client.fetch_users()[:2])

-----------

'''






































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































 