# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
x = house[:]
y = house[:]
for x, y in house :
    print("the " + x + " is " + str(y) + " sqm")