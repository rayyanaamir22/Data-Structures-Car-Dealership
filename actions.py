# ACTIONS 

# Modules
import os
import json

# Other files
import cars as c

# Create a vehicle
def create():    
  # Select a class for the car
  print('SEDAN | SUV | TRUCK | SPORTS CAR')
  while True: # Input verification
    # Select the class of the car
    global carClass
    carClass = input().upper()
    if carClass not in ['SEDAN', 'SUV', 'TRUCK', 'SPORTS CAR']:
      print('Enter an AVAILABLE car class.')
    else:
      os.system('clear')
      break

  if carClass == 'SEDAN':
    classModels = ['CLA', 'E 300']
  elif carClass == 'SUV':
    classModels = ['GLE', 'GLC', 'GLA', 'GLK']
  elif carClass == 'TRUCK':
    classModels = ['G 63', 'X CLASS']
  elif carClass == 'SPORTS CAR':
    classModels = ['AMG GTR', 'AMG ONE', 'SLS', 'SLK']
        
  # Model
  while True:
    global model
    print(classModels)
    model = input('Car model: ').upper()
    if model != '' and model not in classModels:
      print('Enter a valid model from those listed above.')
    elif model in classModels:
      os.system('clear')
      break

  # Year
  global year
  year = 2020

  # Mileage
  global mileage
  if carClass == 'SEDAN':
    mileage = 25
  elif carClass == 'SUV':
    mileage = 60
  elif carClass == 'TRUCK':
    mileage = 80
  elif carClass == 'SPORTS CAR':
    mileage = 50

  # ID
  '''
  sizeOfCatalogue = json.loads(catalogue.json)
  sizeOfPossession = json.loads(possession.json)
  n = len(sizeOfCatalogue) + len(sizeOfPossession)
  global ID
  ID = n
  '''
  
  global carDict
  carDict = {
    "car class" : carClass,
    "model" : model,
    "year" : year,
    "seats" : c.seats,
    "mileage" : mileage,
    "ID" : 1 # temporarily
  }


# Reuse program
def reuse():
  global re
  while True:
    print('Do you want to reuse the program?')
    re = input()
    if re.lower().startswith('y'):
      return True
    elif re.lower().startswith('n'):
      return False
    else:
      print('Invalid input')