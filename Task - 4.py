# Python1 program to find code here creating class circle with constructor
class geeks:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
  # creating list
list = []
  # using list comprehension to append instances to list
list += [geeks(name, roll) for name, roll in [('Akash', 10), ('Deependra', 501), ('Reaper', 22), ('veer', 37), ('Meena', 100), ('prem', 999), ('sandy', 87), ('surya', 351)]]
  # Accessing object value using a for loop
for obj in list:
    print(obj.name, obj.roll, sep=' ')
OUTPUT:
  Akash 10
 Deependra 501
Reaper 22
veer 37
Meena 100
prem 999
sandy 87
surya 351



# Python2 program to find code Create a private class variable named pi= 3.141
    # member variable
    pi = 3.141
    # constructor
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
       # method - name_of_book
    def name_of_Book(self):
        return self.title
     # define an object - Remote control of the class
suman = Book("Kalki", "Prem", 300)
print(suman.title)
OUTPUT: Kalki
   


 
# Python3 program  code to find area and perimeter of rectangle 
  
# Utility function 
def areaRectangle(a, b): 
    return (a * b) 
  def perimeterRectangle(a, b): 
    return (2 * (a + b)) 
  # Driver function 
a = 5; 
b = 6; 
print ("Area = ", areaRectangle(a, b)) 
print ("Perimeter = ", perimeterRectangle(a, b))
OUTPUT:    
Area =  30
Perimeter =  22
