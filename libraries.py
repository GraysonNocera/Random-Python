# Tutorial taken from the internet (not my own)
# This program explores numpy and pandas, two libraries that are essential for 
# machine learning along with other programming problems

import numpy as np
import pandas as pd

# "Numpy tutorial"
# one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
# print(one_dimensional_array)

# two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
# print(two_dimensional_array)

# zeros = np.zeros(5)
# print(zeros)

# # Creates an array from 5 to 11 (not including 12)
# sequence_of_integers = np.arange(5, 12)
# print(sequence_of_integers)

# # Generates random numbers from 50 to 100 (not including 101 but including 50)
# random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6))
# print(random_integers_between_50_and_100)

# # Random floating value between 0.0 and 1.0
# random_floats_between_0_and_1 = np.random.random([6])
# print(random_floats_between_0_and_1) 

# # Adds 2 to every value in random_floats_between_0_and_1
# random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
# print(random_floats_between_2_and_3)

# # Multiplies every value in random_integers_between_50_and_10 by 3
# random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
# print(random_integers_between_150_and_300)

# feature = np.arange(6, 21) # write your code here
# print(feature)
# label = (3 * feature) + 4   # write your code here
# print(label)

# noise = (np.random.random([15]) * 4) - 2   # write your code here
# print(noise)
# label = label + noise    # write your code here
# print(label)

"Pandas Tutorial"
# Create and populate a 5x2 NumPy array.
my_data = np.array([[0, 3], [10, 7], [20, 9], [30, 14], [40, 15]])

# Create a Python list that holds the names of the two columns.
my_column_names = ['temperature', 'activity']

# Create a DataFrame.
my_dataframe = pd.DataFrame(data=my_data, columns=my_column_names)

# Print the entire DataFrame
print(my_dataframe)

# Create a new column named adjusted.
my_dataframe["adjusted"] = my_dataframe["activity"] + 2

# Print the entire DataFrame
print(my_dataframe)

print("Rows #0, #1, and #2:")
print(my_dataframe.head(3), '\n')

print("Row #2:")
print(my_dataframe.iloc[[2]], '\n')

print("Rows #1, #2, and #3:")
print(my_dataframe[1:4], '\n')

print("Column 'temperature':")
print(my_dataframe['temperature'])

data = np.random.randint(low=0, high=101, size=(3, 4))
column_names = ['Eleanor', 'Chidi', 'Tahani', 'Jason']
dataframe = pd.DataFrame(data=data, columns=column_names)
print(dataframe)
print(dataframe['Eleanor'][1])

dataframe['Janet'] = dataframe['Tahani'] + dataframe['Jason']
print(dataframe)

print("Experiment with a reference:")
reference_to_df = dataframe

# Print the starting value of a particular cell.
print("  Starting value of df: %d" % dataframe['Jason'][1])
print("  Starting value of reference_to_df: %d\n" % reference_to_df['Jason'][1])

# Modify a cell in df.
dataframe.at[1, 'Jason'] = dataframe['Jason'][1] + 5
print("  Updated df: %d" % dataframe['Jason'][1])
print("  Updated reference_to_df: %d\n\n" % reference_to_df['Jason'][1])

# Create a true copy of my_dataframe
print("Experiment with a true copy:")
copy_of_my_dataframe = my_dataframe.copy()

# Print the starting value of a particular cell.
print("  Starting value of my_dataframe: %d" % my_dataframe['activity'][1])
print("  Starting value of copy_of_my_dataframe: %d\n" % copy_of_my_dataframe['activity'][1])

# Modify a cell in df.
my_dataframe.at[1, 'activity'] = my_dataframe['activity'][1] + 3
print("  Updated my_dataframe: %d" % my_dataframe['activity'][1])
print("  copy_of_my_dataframe does not get updated: %d" % copy_of_my_dataframe['activity'][1])