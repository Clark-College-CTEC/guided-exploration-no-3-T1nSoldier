# Guided Exploration No. 3
# Brock Sorensen

#Importing the random library for use
import random

#Creating an empty list to fill later
possible_names = []

#Creates the rap-names-output.txt file in write mode and assigns it the outputFile name
outputFile = open('rap-names-output.txt', 'w')

# gives the rap-names.txt file a temporary handle called dataFile
with open('rap-names.txt', 'r') as dataFile:
    # A loop to move names from the dataFile
    for name in dataFile:
        # to the possible_names list
        possible_names.append(name.rstrip())

# user input to tell the program how many names to make
count = int(input('How many rap names would you like to create? '))
# and input telling the program how big the name should be
parts = int(input('How many parts should the name contain? '))

# a for loop that runs the number of times entered by the user
for i in range(count):
    # calling the now filled name_parts list
    name_parts = []
    # another for loop that runs a number of times that the user entered
    for j in range(parts):
        # appends on the corresponding line to a random number between the first and last line
        name_parts.append(possible_names[random.randint(0, len(possible_names)-1)])

    # Uses f string formatting to write the generated names to the outputFile with a line feed at the end.
    outputFile.write(f"{' '.join(name_parts)}\n")
    # prints the same name to the terminal
    print(f"{' '.join(name_parts)}")

# closes the file when finished.
outputFile.close()