# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
file = 'cars.csv'
cars = pd.read_csv(file)

# Print out cars
print(cars)