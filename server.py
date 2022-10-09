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


import main


  
# def add_temps():
#   for i in range(0,100):
#     n = input("Enter temperatures or done:")
#     if n == int:
#       temps.append(n)
#     elif n == "done":
#       break
#     elif():
#       print("error, please type a valid entry")   
#   print(temps)

temperatures = []
def add_temps():
  try: 
    while True:
      temps = temperatures.append(int(input("Enter temperature or done:")))
  except: #anything except number will exit loop
    print(temperatures)


def list_data():
  high = 0
  low = 0
  for temp in temps:
    if temp[0] > high:
      high = temp[0]
    elif temp[0] < low:
      low = temp[0]
  print(high)
  print(low)
  size = len(temperatures)
  print(size)


  





# creating an empty list
# def add_temps():
#   temperatures = []
#   while True:
#     if temperatures == done:
#       break
#     else:
#       temperatures = list(map(int,input("\nEnter the tempatures and end with done : ").strip().split()))
#       print(temperatures)
    

# for i in range(0, done):
#     ele = int(input())
#     temperatures.append(ele) # adding the element
      
# print(lst)

add_temps()







# alternative that didn't match criteria



