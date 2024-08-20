# It lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

# https://www.geeksforgeeks.org/decorator-method-python-design-patterns/?ref=rp

# https://www.youtube.com/watch?v=sIdyTQAlAE8&list=PLwzO627zBnSD2sbolkpJhi7sp4dphcrDF&index=4

# https://refactoring.guru/design-patterns/decorator


# Create an abstract class ICECream having two abstract methods getDescription() and cost()
# Create two concrete classes ChocolateIceCream and ButterScoctchIceCream and another abstract class IceCreamDecorator which extends the abstract class IceCream so that they both will get methods getDescription() and cost()
# Create another abstract class IceCreamDecorator which extends IceCream class and
# Create three other concrete classes choclateSyrupDecorator , RainbowSprinkleDecorator and ChocoChipDecorator which extends class IceCreamDecorator and get  getDescription() and cost() methods