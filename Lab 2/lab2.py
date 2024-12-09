# Alec Porter
# Lab 2
# Computing the Paintable Area of a Basement Floor

# import python math library to use the built-in python value of pi
import math
pi = math.pi

# request user input for floor lenght, floor width, furnace length, furnace width, and heater circumference
floorlength = float(input('Enter the Floor\'s Length in feet: '))
floorwidth = float(input('Enter the Floor\'s Width in feet : '))
furnacelength = float(input('Enter the Furnace\'s Length in inches: '))
furnacewidth = float(input('Enter the Furnace\'s Width in inches: '))
heatercirc = float(input('Enter the Heater\'s Circumference in inches: '))

# calculate floor area in feet
floorarea = floorlength*floorwidth

# calculate furnace area in feet
furnacearea = (furnacelength/12)*(furnacewidth/12)

#calculate heater area in feet
heaterarea = ((heatercirc/12)**2)/(4*pi)

#calculate paintable floor area
paintarea = floorarea-furnacearea-heaterarea

#dispaly paintable floor area
message = 'Paintable Floor Area: {0:.3f} feet.'.format(paintarea)
print(message)




