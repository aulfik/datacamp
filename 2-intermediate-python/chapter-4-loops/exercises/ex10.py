# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for i, j in cars.iterrows() :
    print(i),
    print(j)