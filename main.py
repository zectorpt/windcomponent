import math

print("CrossWind Calculator\n")
print("                _______")
print("               /      /")
print("              /      /")
print("             /      /                 ___")
print("            /      /                 |   |")
print("           /      /                 /    |")
print("         .--------.                |   __\__")
print("(      .'/ /'''''\ '._____________/  /    /")
print(" ( .-----  '''''''                  /    /")
print("  / \                    _______   /----/")
print("  \' >-------||---------'=======''/----/|")
print("   \/-----..-||--------'         /    /  @")
print("    /)    ||(__>                /____/")
print("   /  )  (__>")
print("  /_____/\n")

#Calculate crosswind
def crosswind(a, ws):
	return math.sin(math.radians(a))*ws

#a=Aircraft Heading - Wind direction on METAR

rw = input("Aircraft Heading in degrees: ")
wind = input("Wind direction on METAR: ")
a=rw-wind
ws= input("Wind strength (kt): ")

print("Valor de Crosswind: ", crosswind(a,ws))
