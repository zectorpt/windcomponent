#!/usr/bin/env python
#
# Calculates the Crosswind Component based on input information by user.
# The "Aircraft Heading" can be obtained by the number in the runway. For example, by runway 35 the Aircraft Heading should be 350.
# The "Wind direction on METAR" can be obtained in the METAR. In the example bellow you should use "220".
# The "Wind strength" can be obtained in the METAR. In the example bellow you should use "4".
#
# METAR: LPCS 241100Z 22004KT 180V250 CAVOK 18/11 Q1029
#
# josemedeirosdealmeida@gmail.com
# Jose Almeida

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
