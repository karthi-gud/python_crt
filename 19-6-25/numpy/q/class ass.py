import numpy as np

# sports performance scenario
# a football player goals in 5 matches
# find the average number of goals scored per match using numpy

goals = np.array([1, 0, 2, 3, 1])
average_goals = np.mean(goals)
print("Average number of goals scored per match:", average_goals)

#car mileage tracking scenario
#a car tracks its  mileage over 6 months in km per liter
# #mileage = np.array([15.2,16.9,417.5,18.3,19.0,20.1])
# using numpy find the month where the mileage is less than the 16 km per liter
mileage = np.array([15.2, 16.9, 17.5, 18.3, 19.0, 20.1])
low_mileage_months = np.where(mileage < 16)
print("Months with mileage less than 16 km/l:", low_mileage_months[0] + 1)  # Adding 1 to convert index to month number
# Calculate the total mileage for the car over the 6 months
total_mileage = np.sum(mileage)
print("Total mileage over 6 months:", total_mileage)
# Calculate the average mileage over the 6 months
average_mileage = np.mean(mileage)
print("Average mileage over 6 months:", average_mileage)
# Calculate the month with the highest mileage
highest_mileage_month = np.argmax(mileage) + 1  # Adding 1 to convert index to month number
print("Month with highest mileage:", highest_mileage_month)
