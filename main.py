'''
Name: Rayyan Aamir
Date: April 21, 2022
Program: Car Dealership (Data Structures Project)
'''

# Modules
import os
import json

# Other files
import actions as a # System functions
import cars as c # Objects
import fileHandling as h # Reading and writing functions

'''
Description:
This program is meant to replicate the purchase/return procedure of a car being sold in a dealership. Each process either purchases or returns the selected car, and moves it between the files "catalogue.json" and "possession.json". The cars' information are stored as dictionaries, which are assigned as key-value pairs in the json dictionaries. The purchase function is fully operational, but the return function cannot work at the same time since, when cars are moved between files, the format of the json file changes. If you want to reset the program, copy and paste the "___Backup.json" file into the actual.
'''

# PROGRAM START
while True:
  # Main menu

  # Record JSON objects as dictionaries in Python
  possession = json.dumps("possession")
  pDict = json.loads(possession)
  
  catalogue = json.dumps("catalogue")
  cDict = json.loads(catalogue)
  
  # User selects action
  global action
  while True:
    print('CAR DEALERSHIP')
    
    print('\nDo you want to CREATE, VIEW, PURCHASE, or RETURN a vehicle?')
    action = input().upper()
    if action in ['CREATE', 'VIEW', 'PURCHASE', 'RETURN']:
      break
    else:
      os.system('clear')
  os.system('clear')
  
  # Create a car
  if action == 'CREATE':
    # Car creationg function

    # This does not work, maybe creating a car should happen outside of the class, as it is not a method of a car.
    a.create()

    # Append data of newly created car to catalogue json
    h.writeToCatalogue(a.carDict)
      

  # Examine an owned car
  elif action == 'VIEW':
    h.displayPossession()


  # Purchase a new car
  elif action == 'PURCHASE':
    # DISPLAY CATALOGUE
    h.displayCatalogue()
    
    # Purchase procedure
    h.purchaseCar()

    # Conclude purchase by appending the car to possession.txt

    # Remove purchased car from catalogue
    
    
    # Return an owned car
  elif action == 'RETURN':
    while True:
      # Show the car in user's possession
      h.displayPossession()

      # User selects which car they are returning
      h.returnCar()
          

      # Remove car from possession and add to catalogue
    

  
  # Reuse code
  if a.reuse():
    os.system('clear')
    continue
  else:
    os.system('clear')
    print('Goodbye.')
    break