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


temp_list = []

def add_temps():
  while True:
      user_input = input("Enter the tempatures and end with done : ")

      if user_input == 'done':
          break

      try:
          temp_list.append(int(user_input))
      except ValueError:
          print('Invalid entry.')
          continue

  print(temp_list)
  

def list_data():
  high = 0
  low = 0
  for temp in temp_list:
    if temp[0] > high:
      high = temp[0]
    elif temp[0] < low:
      low = temp[0]
  print(high)
  print(low)
  size = len(temp_list)
  print(size)
  
  
add_temps()
list_data()

