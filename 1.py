A= 1_0_0_0
B = 1000
Total = A*B
print(Total)







# List 
lst = ["STRING", 1,2,3,["A new item"], "Rakesh"]
print(lst)
for item in lst:
    print("The item is :",item)
names = ["rakesh", "Aryan"]
for name in names:
    print("Name",name)


names.append("PINKY")
names.append("Rashmi")


for name in names:
    print("NAME",name)


# It gets the last member 
ras = names.pop()
print(ras)









# Dictionary

person = {"key":"value",
          
          "name": "Rakesh",
          "twitter":"@AlbertRakesh",
          "fb": "@RakeshNaik"

}


for per in person:
    print("Person",per)


print(person["key"])

person ["home"]= "Pikrijrana"


for per in person:
    print(per)

del person["fb"]


for per in person:
    print(per)






#Dictionary within Dictionary

students = {"Rakesh": {"Math":95, "Science":80}, "Rashmi":{"Math":92, "Economics":80}}
for stud in students:
    print(stud)

print(students["Rakesh"])
print(students["Rashmi"])







#Tuple is immutable (Not changable)

foods = ("Pizza", "Orange", "Apple", "Pasta")
print(foods)
for food in foods:
    print("The food is:", food)





# Set (Don't maintain order)
s = {"A", "Apple", "Rakesh"}
print(s)


# Boolean
Hey = "Rakesh"
if Hey:
    print("True")

Rakesh = 1
if Rakesh :
    print("Yeah working")


# NONE

wallet = None

if wallet is None:
    print("There is nothing in my wallet")

##Slicing and Indexing


rakeshlist = ["Rakesh","Aryan","Pinky","Rashmi","Sneeti"]
# indexing    0,          1,     2,        3,        4
# BackIndex  -5,         -4,    -3,       -2,      ,-1


print(rakeshlist[3])
print(rakeshlist[0:3])# goes upto the 3rd not include the 3rd(Goes like 0,1,2 index)
print(rakeshlist[0::])#goes till the end
print(rakeshlist[0::])#goes till the end
print(rakeshlist[-1::])
print(rakeshlist[-5::])
print(rakeshlist[-6::])
print(rakeshlist[::-1])#write backward
print(rakeshlist[::-4])#write backward
print(rakeshlist[::-3])#write backward



#Accepting User Input
age = input(" What is your age: ")
print("You're age is : ", age)

name = input ("What's your name buddy:")
print("Helllooooooooo........", name, "Your Age is : ", age)


# type casting 
age = input ("What's your age? ")
data_type = type(age)
print(data_type)

age = int(age)
data_type = type(age)
print(data_type)

# Print Formatting 
name= "Rakesh"
welcome_messages = "Hello {} Welcome to Python 101".format(name)
print(welcome_messages)

welcome_messages = f"Hello {name} Welcome to Python 101"
print(welcome_messages)