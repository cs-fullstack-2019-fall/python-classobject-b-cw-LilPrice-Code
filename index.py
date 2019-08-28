def main():
    # pro1()
    # pro2()
    pro3()
# Problem 1:
#
# Create a class Dog. Make sure it has the attributes name, breed, color, gender. Create a function that will print all attributes of the class. Create an object of Dog in your problem1 function and print all of it's attributes.
#
def pro1():
    class Dog:
        def __init__(self,name,breed,color,gender):
            self.name = name
            self.breed = breed
            self.color = color
            self.gender = gender

        def printall(self):
            return (f"{self.name}\n{self.breed}\n{self.color}\n{self.gender}")

    d1 = Dog("Max", "Pitbull","White","Male")
    print(d1.printall())

# Problem 2:
#
# We will keep having this problem until EVERYONE gets it right without help
#
# Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign, ask them to input another string.
#
def pro2():
    def theLoop():
        user = ""
        while user != "=":
            user = input("Enter something\n")
    theLoop()
# Problem 3:
#
# Create a class Product that represents a product sold online. A product has a name, price, and quantity.
#
# The class should have several functions:
#
# a) One function that can change the name of the product.
#
#     b) Another function that can change the name and price of the product.
#
#     c) A last function that can change the name, price, and quantity of the product.
#
#     Create an object of Product and print all of it's attributes.
def pro3():
    class Product:
        def __init__(self,name,price,quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        def changeName(self,newName):
            self.name = newName

        def twoChange(self,nName,nPrice):
            self.name = nName
            self.price = nPrice

        def changeAll(self,Rname,Rprice,Rquantity):
            self.name = Rname
            self.price = Rprice
            self.quantity = Rquantity

    p1 = Product("Football", 23, 2)
    p1.changeName('Soccer')
    print(p1.name)
    p1.twoChange("Baseball", 10)
    print(p1.name)
    print(p1.price)
    p1.changeAll("Bastketball", 30,3)
    print(p1.name)
    print(p1.price)
    print(p1.quantity)


main()