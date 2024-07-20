class Vehicle:
    def __init__(self,mil , speed, cap):
        self.max_milage = mil
        self.max_speed = speed
        self.capacity = cap

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        return super().fare() + 0.1*super().fare()
    
b = Bus(10,30,50)
print(b.fare())