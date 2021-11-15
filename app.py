import math
course = 'python for beginners'
print(course[0:-18])
print(len(course))
print(course.upper())
print (course.lower())
print(course.find('b')) 
print(course.replace('beginners','not beginners'))
print(course.replace('b','k'))
print('rat' in course)
print(2.9 ** 5)
x = 5
y = 10
print(round(x))
print(abs(x))
print(math.ceil(x))
print(math.floor(x))
print(math.factorial(x))
print(math.fmod(x,y))
has_good_credit = True 
has_criminal_record = True
if  has_good_credit and not has_criminal_record:
	print("eligible for loan")
temperature = 30
if temperature > 30 :
	print("hot day")
else:
	print("not a hot day")
weight = input("weight: ")
unit = input("L(lbs) or K(kg): ")
if unit.upper() == "L":
	converted = weight * 0.45
	print("you are {converted} kilograms")
else :
	unit.upper() == "K"
	converted = weight/0.45
	print("you are {converted} pounds")