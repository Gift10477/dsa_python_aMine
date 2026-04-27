class Product:
    def __init__(self, name, product_price, product_desc):
        self.name = name
        self.product_price = product_price
        self.product_desc = product_desc
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
p1 = Product("Laptop", 1000, "A high-performance laptop")
print(p1.get_name()) 