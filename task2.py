from abc import ABC,abstractmethod
class vehicle:
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

class car(vehicle):
    def start(self):
        print("\ncar satrted")

    def stop(self):
        print("car stoped")

    def fuel_type(self):
        print("petrol\n")

class bike(vehicle):
    def start(self):
        print("bike satrted")

    def stop(self):
        print("bike stoped")

    def fuel_type(self):
        print("petrol\n")

class tesla(vehicle):
    def start(self):
        print("tesla satrted")

    def stop(self):
        print("tesla stoped")

    def fuel_type(self):
        print("electric\n")


c = car()
c.start()
c.stop()
c.fuel_type()

b = bike()
b.start()
b.stop()
b.fuel_type()

t = tesla()
t.start()
t.stop()
t.fuel_type()
