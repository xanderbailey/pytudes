import math

with open("ex1.txt",'r') as f:
	modules = [int(line.split("\n")[0]) for line in f]

def calculate_fuel_from_mass(mass):
	fuel = math.floor(mass/3) - 2
	return fuel

#def calculate_fuel_from_fuel(new_fuel)

total_fuel = 0
for module in modules:
	total_fuel += calculate_fuel_from_mass(module)
	total_new_fuel = 0	
	new_fuel = calculate_fuel_from_mass(calculate_fuel_from_mass(module))
	total_new_fuel += new_fuel 
	while max(new_fuel,0) > 0:
		new_fuel = calculate_fuel_from_mass(new_fuel)
		total_fuel += max(new_fuel,0)
	total_fuel += total_new_fuel

print(total_fuel)

