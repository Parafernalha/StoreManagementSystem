import csv


class Item:


    pay_rate = 0.8 # Pay rate applied in a 20% discount

    all = []

    def __init__(self, name: str, price:float, quantity=0): # Constructor method

       
        assert price >= 0, f"price {price} is not greater than or equal to zero!" # Beautiful of the Assert = Throw an exception with a comment that WE choose
        assert quantity >= 0, f"Quantity {quantity} can't be less than zero!"

        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Action to execute

        Item.all.append(self)

         #Encapsulation
    @property
        #property Decorator = Read-only Attribute
    def price (self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

                

        #Encapsulation
    @property
        #property Decorator = Read-only Attribute
    def name (self):
        return self.__name

        #Another decorator used in the ecanpsulation process, where we can set values if the input value match our conditionals
    @name.setter
    def name(self,value):
        if len(value)>10:
           raise Exception("The name is too long") #
        else:
           self.__name = value


       
    def Total_price (self,__price=0,quantity=0):
        return self.__price*self.quantity
        
        # Using one more magic method called __repr__ to represent our objects
    def __repr__(self):
        return f"{self.__class__.name}('{self.name}',{self.__price},{self.quantity})" #'' to escape of the "" used externally
   
    #
    @classmethod
    def instantiate_from_CSV(cls):
        with open('StoreManagementSystem/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                Item(
                    name=item.get('name'),
                    __price=float(item.get('__price')),
                    quantity=int(item.get('quantity')),
                    )

    @staticmethod
    def is_integer(num):
        #We will count out the floats that are point zero
        #For i.e: 5.0, 10.0
        if isinstance(num, float):
            #Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
            
    #@property #Decorators: function that you can pre-execute before another function
    #def read_only_name(self):
    #    return "AAA"

    #Creating a child class

class Phone(Item): #What class will i inherited for? ans: Item

    def __init__(self, name: str, __price:float, quantity=0, broken_phones=0): # Constructor method
         
        super().__init__(name,__price,quantity) #give access to the methods and attributes of the parent class.
        

        #Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero."
        
       #Assign to self object
        self.broken_phones = broken_phones




 