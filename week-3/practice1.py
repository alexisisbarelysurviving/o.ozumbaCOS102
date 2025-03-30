city_1 = input('Enter name of city 1: ')
city_2 = input('Enter name of city 2: ')

temp = city_1
city_1 = city_2
city_2 = temp 

print (f"the name of city 1 after swapping is {city_1}")
print (f"the name of city 2 after swapping is {city_2}")