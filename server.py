#DSC 510
#Week 6
#Programming Assignment Week 6 strings and lists
#Author Dave Lingerfelt
#10/8/22


import main
print(main.main("hello"))

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
  high = temp_list[0]
  low = temp_list[0]
  for temp in temp_list:
    if temp > high:
      high = temp
    elif temp < low:
      low = temp
  print(high)
  print(low)
  size = len(temp_list)
  print(size)
  
  
add_temps()
list_data()

