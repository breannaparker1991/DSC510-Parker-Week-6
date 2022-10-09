#DSC 510
#Week 6
#Programming Assignment Week 6 strings and lists
#Author Dave Lingerfelt
#10/8/22


# Your program must have a properly defined main method and a properly defined call to main.
# Create an empty list called temperatures.
# Allow the user to input a series of temperatures along with a sentinel value (do not use a number for a sentinel value) which will stop the user input.
# Evaluate the temperature list to determine the largest and smallest temperature.
# Print the largest temperature.
# Print the smallest temperature.
# Print a message that tells the user how many temperatures are in the list.

temperatures = []

def temps():
  while True:
    temperatures.append(int(input("Enter temperature or done:")))

