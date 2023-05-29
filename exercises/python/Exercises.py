# 8.1a
# loop

for count in range(10):
    print('Oliver Sperlik 304131')

# 8.1b
# input

wish = input("Enter your wish: ")
repetitions = input("Enter amount of repetitions: ")

for count in range (int(repetitions)):
    print(wish)

# 8.2
# imperative
# sum

numList = [1, 2, 3, 4, 5]
sumImperative = 0
for num in numList:
    sumImperative = sumImperative + num
print (sumImperative)

# 8.3

# imperative
# input

userInput = 0
while (userInput != 123):
    userInput = input("Enter number: ")
    userInput = int(userInput)
    if ((userInput % 2) == 0):
        print(userInput)
print("Bye for now")

# 8.4

# imperative
# group list

def group_list(list, glength):
    result = []
    for index, _ in enumerate(list):
        if (index % glength == 0):
            result.append(list[index: index+glength])
    return result
print(group_list([1, 2, 3, 4, 5, 6], 2))

# 8.5
# dict

dict = {
    "Bob the Builder": "IoT",
    "Dora the Explorer": "Interactive Media",
    "Paw Patrol": "Data Engineering"
}

dict["Bob the Builder"] = "Data Engineering"
dict["Farmer Pickles"] = "Climate Engineering"
print(dict["Dora the Explorer"])
print(dict)

# 8.6
# i am pretty sure you cant solve this with just what is said in the pdf


# 9.1
# oop
# inheritance
# property
# get set
# polymorphism
# class
# object

class MyRecipe:

    @property
    def calories(self):
        return self.__calories
    @calories.setter
    def calories(self, value):
        self.__calories = value

    @property
    def cooking_time(self):
        return self.__cooking_time
    @cooking_time.setter
    def cooking_time(self, value):
        self.__cooking_time=value

    def __init__(self, calories, cooking_time):
        self.__calories = calories
        self.__cooking_time = cooking_time

    def cook(self):
        print(f'cooking time: {self.cooking_time}, calories: {self.calories}')

recipe = MyRecipe(900, 5)
recipe.cook()
recipe.cooking_time = 10
recipe.cook()

# 9.2

class Contact:

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        self.__email = value

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def __str__(self):
        return f'name: {self.name}, email: {self.email}'


class AddressHolder:

    @property
    def street(self):
        return self.__street
    @street.setter
    def name(self, value):
        self.__street = value
    
    @property
    def postcode(self):
        return self.__postcode
    @postcode.setter
    def postcode(self, value):
        self.__postcode = value

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, value):
        self.__city = value

    def __init__(self, street, postcode, city):
        self.__street = street
        self.__postcode = postcode
        self.__city = city
    
    def __str__(self):
        return f'address: {self.street}, postcode: {self.postcode}, city: {self.city}'

class Friend(Contact, AddressHolder):
    
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, value):
        self.__phone = value
    
    def __init__(self, name, email, street, postcode, city, phone):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, postcode, city)
        self.__phone = phone
        
    def __str__(self):
        Contact.__str__(self)
        AddressHolder.__str__(self)
        return f'{Contact.__str__(self)} {AddressHolder.__str__(self)} phone: {self.phone}'


friend = Friend("1", "11", "111", "1111", "11111", "111111")

print(friend)

# 9.3

class Fish:
    def eat(self):
        print(f'I am a swimming fish')
    def swim(self):
        print(f'I am an eating fish')

class Shark(Fish):
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def place_found(self):
        return self.__place_found
    @place_found.setter
    def place_found(self, value):
        self.__place_found = value

    def swim(self):
        print(f'I am shark eating named {self.name}')
    
    def eat(self):
        print(f'I am a shark swimming at {self.place_found}')

    def __init__(self, name, place_found):
        self.__name = name
        self.__place_found = place_found


class Dolphin(Fish):
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    def swim(self):
        print(f'I am a swimming dolphin')

    def eat(self):
        print(f'I am a dolphin eating named {self.name}')

    def __init__(self, name):
        self.__name = name

fish = Fish()

fish.eat()
fish.swim()

shark = Shark("Kokot", "V pici")

shark.eat()
shark.swim()

dolphin = Dolphin("Vyjebanec")

dolphin.eat()
dolphin.swim()

# 9.4
from abc import ABC, abstractmethod

class CaffeineDrink(ABC):
    
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, value):
        self.__description = value
        
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        self.__size = value
        
    def __init__(self, description, size):
        self.__description = description
        self.__size = size
        
    def drink_info(self):
        print(f'size: {self.size}, description: {self.description}')
        
    @abstractmethod
    def get_price():
        pass
    
class Coffee(CaffeineDrink):
    
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
    
    @property
    def tax_rate(self):
        return self.__tax_rate
    @tax_rate.setter
    def tax_rate(self, value):
        self.__tax_rate = value
    
    def __init__(self, description, size, quantity, tax_rate):
        CaffeineDrink.__init__(self, description, size)
        self.__quantity = quantity
        self.__tax_rate = tax_rate
        
    def get_price(self):
        return (5 * self.quantity * self.size) * ((self.tax_rate/100) + 1)
    
    
    
class Tea(CaffeineDrink):
    
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
        
    def __init__(self, description, size, quantity):
        CaffeineDrink.__init__(self, description, size)
        self.__quantity = quantity
        
    def get_price(self):
        return self.quantity * 4 * self.size
        
coffee = Coffee("Latte", 1.2, 2, 20)

print(coffee.get_price())

# 10.1a
# functional
# sum list
num_list = [1, 2, 3, 4, 5]

def fun_list_sum(list, iteration = 0, sum = 0):
    if (iteration == len(num_list)):
        return sum
    return fun_list_sum(list, iteration + 1, sum + num_list[iteration])

print(fun_list_sum(num_list))

# 10.1b
# lambda
# ternary
num_list = [1, 2, 3, 4, 5]

fun_list_sum = lambda list, iteration = 0, sum = 0 : sum if (iteration == len(num_list)) else fun_list_sum(list, iteration + 1, sum + num_list[iteration])
        
print(fun_list_sum(num_list))

# 10.2a
# recursion
# factorial
# lambda

recursive_factorial = lambda num : 1 if (num == 0) else num * recursive_factorial(num - 1)
print(recursive_factorial(5))

# 10.2b
# square sum
# recursion
# lambda
square_sum = lambda int1, int2 : ((int1*int1) + (int2*int2))
print(square_sum(3, 4))

# 10.3

# print even numbers
# lambda
# filter

print_even_numbers = lambda list : filter(lambda x: x % 2 == 0, list)
print(list(print_even_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 10.4

# sort
# lambda

gtg_sales = [
    ('Coffee', 2018, 525.05),
    ('Juice', 2021, 526.03), 
    ('Apple', 2020, 525.12), 
    ('Green Tea', 2019, 525.02), 
    ('Banana', 2022, 524.08)
    ]
    

print(sorted(gtg_sales, key = lambda el: el[1]))



    

    