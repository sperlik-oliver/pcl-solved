# 7a

# sum list
# imperative

num_list = [1, 2, 3, 4, 5]

def sum_list(list):
    sum = 0
    for x in list:
        sum = sum + x
    return sum
print(sum_list(num_list))

# 7b

# input
# imperative

user_input = 0
print("Welcome to even numbers printer. Input 123 to exit")
while (user_input != 123):
    user_input = int(input("Enter number: "))
    if (user_input % 2 == 0):
        print(f'{user_input} is even')
print("Bye for now!")

# 8a

# map
# lambda
# add 10
# add ten

data = [1, 2, 3, 4, 5]

add_ten = lambda list_to_add: list(map(lambda x: x + 10, list_to_add))

print(add_ten(data))

# 8b

# find even
# filter

data = [1, 2, 3, 4, 5]

find_even = lambda list_to_filter: list(filter(lambda x: x % 2 == 0, list_to_filter))

print(find_even(data))

# 9a

# group list
# imperative
# enumerate

def group_list(list, glength):
    result = []
    for index, _ in enumerate(list):
        if (index % glength == 0):
            result.append(list[index: index+glength])
    return result
print(group_list([1, 2, 3, 4, 5, 6], 2))
        

# 9b

# filter by string
# characters
# imperative

dk_cities = ['Copenhagen', 'Aarhus', 'Aalborg', 'Horsens', 'Odense']

def filter_cities(cities):
    filtered = []
    for city in cities:
        if (city[0:2] == 'Aa'):
            filtered.append(city)
    return filtered
print(filter_cities(dk_cities))

# 10a

# oop
# class
# property
# get set
# inheritance
# polymorphism

from datetime import datetime

class Notebook:

    @property
    def course_notes(self):
        return self.__course_notes
    @course_notes.setter
    def course_notes(self, value):
        self.__course_notes = value

    def search(self, searchFilter):
        return list(filter(lambda el: el.isAMatch(searchFilter), self.course_notes))
    
    def addNote(self, jotting, keywords):
        self.__course_notes.append(CourseNote(jotting, keywords))
    
    def __init__(self):
        self.__course_notes = []

class CourseNote:

    @property
    def jotting(self):
        return self.__jotting
    @jotting.setter
    def jotting(self, value):
        self.__jotting = value

    @property
    def creation_date(self):
        return self.__creation_date
    @creation_date.setter
    def creation_date(self, value):
        self.__creation_date = value

    @property
    def keywords(self):
        return self.__keywords
    @keywords.setter
    def keywords(self, value):
        self.__keywords = value

    def __init__(self, jotting, keywords):
        self.__jotting = jotting
        self.__keywords = keywords
        self.__creation_date = datetime.today().strftime('%Y-%m-%d')
    
    def isAMatch(self, searchFilter):
        return searchFilter in self.jotting or searchFilter in self.keywords
        
    def __str__(self):
        return f'jotting: {self.jotting}, creation date: {self.creation_date}, keywords: {self.keywords}'
    
    def __repr__(self):
        return self.__str__()
    

notebook = Notebook()
notebook.addNote("Picoviny riadne su to", "Kurva, Kokot")
notebook.addNote("Jebem to", "Pica, Jebo")

print(notebook.search("Picoviny"))
print(notebook.search("Jebo"))

# 10b

class Singer:
    def sing(self):
        print('I am singing')

class Songwriter:
    def compose(self):
        print('I am songwriting')

class SingerSongwriter(Singer, Songwriter):
    def strum(self):
        print('I am strumming')
    def actSensitive(self):
        print("I am acting sensitive")

singerSongwriter = SingerSongwriter()
singerSongwriter.sing()
singerSongwriter.compose()
singerSongwriter.strum()
singerSongwriter.actSensitive()
