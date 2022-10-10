my_list = []

def asd():
  while True:
      user_input = input('Enter a number: ')

      if user_input == 'done':
          break

      try:
          my_list.append(int(user_input))
      except ValueError:
          print('Invalid number.')
          continue


  print(my_list)
  
asd()