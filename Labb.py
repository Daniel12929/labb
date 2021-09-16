import math

x_kub = float(input("Enter the length of the sides of your cube (in cm): "))
x_tetra = float(input("Enter the edge length of your tetrahedron (in cm): "))

volkub = x_kub ** 3
voltetra = (x_tetra ** 3) / (6 * math.sqrt(2))

print("Your cube is " + str(volkub) + " cubic cm and your tetrahedron is " + str(voltetra) + " cubic cm")