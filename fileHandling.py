# File handling functions

# Modules
#from asyncio.windows_events import NULL
import json
# from xxlimited import Null

# POSSESSION
def writeToPossession(newData, filename='possession.json'):
  with open(filename, 'r+') as file:
    # Load data into a dictionary
    fileData = json.load(file)
    
    # Join data with json file
    fileData["ownedCars"].append(newData)

    # Set file's current position at offset
    file.seek(0)

    # Convert back to json
    json.dump(fileData, file, indent = 4)

def displayPossession():
  print('Garage:\n')
  file = open('possession.json')
  data = json.load(file)
  n = 1
  n = 1
  for carId in data:
      print (n,'.', end = '')
      for carDetails in data[carId]:
        print('\t{0}: {1}' .format(carDetails, data[carId][carDetails]))
      n += 1
      print()

  file.close()

# CATALOGUE
def writeToCatalogue(newData, filename='catalogue.json'):
  with open(filename, 'r+') as file:
    # Load data into a dictionary
    fileData = json.load(file)
    
    # Join data with json file
    fileData["carsForSale"].append(newData)

    # Set file's current position at offset
    file.seek(0)

    # Convert back to json
    json.dump(fileData, file, indent = 4)

def displayCatalogue():
  print('Showroom:\n')
  file = open('catalogue.json')
  showroom = json.load(file)
  n = 1
  for carId in showroom:
      print (n,'.', end = '')
      for carDetails in showroom[carId]:
        print('\t{0}: {1}' .format(carDetails, showroom[carId][carDetails]))
      n += 1
      print()
  file.close()

# PURCHASE AND RETURN

def SaveCarsToCatalogue(newCarInventory):
    with open('catalogue.json', 'w') as outfile:
      json.dump(newCarInventory, outfile)

def SaveCarToPossession(newPosessions):
    with open('possession.json', 'w') as outfile:
      json.dump(newPosessions, outfile)

# Purchase procedure
def purchaseCar():
  # Select car to purchase
  print('Enter the ID of the car to be purchased:')
  try:
    userInputPurchaseID = int(input())
    cdata = json.load(open('catalogue.json'))
    newData = {}
    purchasedCar = None
    purchasedCarId = -1
    # Verify if ID is present
    for carId in cdata: # ['carsForSale']:
        if (int(carId) != userInputPurchaseID):
            newData[carId] = cdata[carId]
            # newData.append(car)
        else:
            purchasedCarId = carId
            purchasedCar = cdata[carId]

    SaveCarsToCatalogue(newData)

    if (int(purchasedCarId) >= 0):
      # load possession.json data into a dictionary
      pdata = json.load(open('possession.json'))
      # add the new purchasedCar at the end of that dictionary
      pdata[purchasedCarId] = purchasedCar
      # write back to possession
      SaveCarToPossession(pdata)
      print ('Car {0} marked as sold. Entry moved from Catalogue to Possession.' .format(purchasedCarId))
    else:
      print ('Car no longer available. Car with ID {0} does not exist.' .format(purchasedCarId))

  except ValueError:
    print('Invalid ID. Please Enter a valid ID.')


# Return procedure
def returnCar():
  # Select car to return
  print('Enter the ID of the car to be returned:')
  while True:
    try:
      purchaseID = int(input())
      data = json.load(open('possession.json'))
      # Verify if ID is present
      for i in range(len(data)):
        if data[i]["ID"] == purchaseID: # If it is
          destination = json.load('catalogue.json')
          destination["carsForSale"].append(i)
          data.pop[i]
          break # Continue on
        else: # If not
          raise ValueError # Run ValueError code
    except ValueError:
      print('Enter a valid ID.')

  print('ID was valid!')