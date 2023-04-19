class VideoCard:
    def __init__(self, name, brand, memory, price):
        self.name = name
        self.brand = brand
        self.memory = memory
        self.price = price
    def __str__(self):
        return f"{self.name} ({self.brand}), {self.memory}GB, ${self.price:.2f}"
