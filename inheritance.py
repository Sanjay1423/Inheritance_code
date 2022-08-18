
# ? Inheritance
# Inheritance is a way of obtaining properties such as attributes and methods from another class

# ? Why we use inheritance
# Inheritance  increase the reusability of the code and readiblity of the code

# ? Types of Inheritance

# Single Level inheritance
# Multilevel inheritance
# Multiple inheritance
# Heirarchichal inheritance

# ? Inheritance examples

# ! single level inheritance

class Parent:
    pass


class Child(Parent):
    pass


# ! Mutli Level Inheritance

class Grand_parents:
    pass


class Parents(Grand_parents):
    pass


class Child(Parents):
    pass


# ! Heirarchichal Inheritance

class Parents:
    pass


class Child_1(Parents):
    pass


class Child_2(Parents):
    pass


# ! Multiple Inheritance

class Father:
    pass


class Mother:
    pass


class Child(Father, Mother):
    pass


# ! Inheritance Real World Example

class Bike:
    def __init__(self, color, mileage, manufactured_year):
        self.color = color
        self.mileage = mileage
        self.manufactured_year = manufactured_year

    def mileage_test(self):
        if self.mileage < 50:
            return "Very low"
        else:
            return "Good"


class Perfomance:
    def __init__(self, CC, max_speed):
        self.CC = CC
        self.max_speed = max_speed

    def speed_test(self):
        if self.max_speed < 100:
            return "Very low"

        elif self.max_speed > 100 and self.max_speed < 150:
            return "Good"

        else:
            return "Excellent"


class Petrol_bike(Bike):
    def __init__(self, color, mileage, manufactured_year, engine_type):
        super().__init__(color, mileage, manufactured_year)
        self.engine_type = engine_type


class Electric_bike(Bike):
    def __init__(self, color, mileage, manufactured_year, battery_type):
        super().__init__(color, mileage, manufactured_year)
        self.battery_type = battery_type


class R15(Bike, Perfomance):
    def __init__(self, color, mileage, manufactured_year, CC, max_speed):
        Bike.__init__(self, color, mileage, manufactured_year)
        Perfomance.__init__(self, CC, max_speed)


r15 = R15('red', 40, 2020, 200, 180)
print(r15.mileage_test())
print(r15.speed_test())
print(r15.color)
