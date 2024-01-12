# Start
# Create a function called 'average_calculation' that calculates the average of the items in a list.
# Create a function called 'variance' to calculate the variance (square of the difference of the values and the means).
# Create a function called 'standard_deviation' that is the square root of the variance.
# Create a dictionary called 'locations' which stores the different radiation levels in a list for each of the locations.
# For each of the locations in the dictionary:
    # Display the average radiation level.
# For each of the locations in the dictionary:
    # Display the standard deviation of the radiation levels.
# While a user would like to enter a new radiation level to locations:
    # If a user enters 'Done':
        # Debug and exit the programme.
    # Else, if a user decides to type one of the locations in the dictionary:
        # Whilst a user wishes to enter values for the location they have chosen to enter values for:
            # if the user enters 'Done':
                # Exit this loop to enable the user to choose another location to enter values for
                # or to exit the programme altogether.
            # When the user enter a radiation level:
                # Add the new values to the list of the chosen location (key-value pair) from the dictionary.
            # However, if the user enters anything except 'Done' or an integer:
                # Display that the input could not be recognised and ask the user to try again.
# If the length of the list in the locations dictionary exceeds the original length (5):
    # for each location in the locations dictionary:
        # Calculate and display the average radiation levels including the new values that the user has entered.
    # for each location in the locations dictionary:
        # Calculate and display the standard deviation radiation levels including the new values that the user has entered.
# Otherwise:
    # Inform the user that no new values were entered.
# End

def average_calculation(levels):
    return (sum(levels)/len(levels))

def variance(levels):
    means = average_calculation(levels)
    return average_calculation([(i - means)**2 for i in levels])

def standard_deviation(levels):
    return (variance(levels))**0.5

locations = {"City Centre" : [22, 19, 20, 31, 28],
             "Industrial Zone" : [35, 32, 30, 37, 40],
             "Residential District" : [15, 12, 18, 20, 14],
             "Rural Outskirts" : [9, 13, 16, 14, 7],
             "Downtown" : [25, 18, 22, 21, 26]
            }
            
for location, levels in locations.items():
    # Debugging: Prints the location and levels being processed.
    print("\nDebug: Processing location {} with radiation levels {}".format(location, levels))
    print("{} Average Radiation Level: {:.2f}".format(location, average_calculation(levels)))

for location, levels in locations.items():
    # Debugging: Prints the location and levels being processed.
    print("\nDebug: Processing location {} with radiation levels {}".format(location, levels))
    print("Standard Deviation of Radiation Levels in the {}: {:.2f}".format(location, standard_deviation(levels)))

# In order to allow for continuous data input, a while loop has been used below.
# This loop runs indefinitely until 'Done' is entered.

while True:

    location = input("\nPlease enter the location you would like to add a new radiation level to or 'Done' to finish: ").title()
    if location == "Done":
        # Debugging: Confirms that the loop exit condition has been met.
        print("Debug: Exiting input loop.")
        print("Goodbye.")
        break
    elif location in locations:
        
        while True:
            try:
                level_or_done = input('''
Please enter the radiation level or type 'Done' to enter a new radiation level for one of the other locations: ''').title()
                if level_or_done == "Done":
                    break
                # Converts the input to a float.
                level = float(level_or_done)
                # Adds to the levels list that the user has entered that is available in the 'locations' dictionary.
                locations[location].append(level)
                # Debugging: Confirms that a new level has been added
                print("Debug: Added level {} to {}.".format(level, location))
            except ValueError:
                # Debugging: Informs the user of an invalid input.
                print("Sorry, your input could not be recognised. Please try again.")

# After exiting the loop, the following code calculates and displays the new average radiation levels 
# and standard deviation depending on the user input.
    if len(locations[location]) > 5:
        for location, levels in locations.items():
            print("{} New Average Radiation Level: {:.2f}".format(location, average_calculation(levels)))

        for location, levels in locations.items():
            print("New Standard Deviation of Radiation Levels in the {}: {:.2f}".format(location, standard_deviation(levels)))
    else:
        # Debugging: Informs the user that no new measurements were entered.
        print("Debug: No new measurements were entered.")

# An alternate way that could be explored without using defined functions is enumerate.
# An example of how the average of the different location's radiation levels would be found using the enumerate() function
# is below:
'''locations = ["City Centre", "Industrial Zone", "Residential District", "Rural Outskirts", "Downtown"]
levels = [[22, 19, 20, 31, 28], [35, 32, 30, 37, 40], [35, 32, 30, 37, 40], [9, 13, 16, 14, 7], [25, 18, 22, 21, 26]]
for i, location in enumerate(locations):
   # Debugging: Prints the location and levels that are being processed.
    # print("Debug: Processing location {} with levels {}". format(location, levels[i]))
    average = sum(levels[i])/len(levels[i])
    print("{} Average Radiation Level: {}".format(location, average))'''