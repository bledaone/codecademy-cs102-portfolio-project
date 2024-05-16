import os
import random
import restaurantData


def clear_screen():
    # Check if the system is Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Call the function to clear the screen
clear_screen()

print("Hello, there. Here is the menu for today: ")

for index, resto in enumerate(restaurantData.types, start=1):
    print(f"{index:02}. {resto.capitalize()}")

resto_start = input("Please select a restaurant by typing the first several letters of the restaurant type ... ")
print(f"You typed \"{resto_start}\" ... processing ...")

print("Here is a list of restaurants that match your search: ")

# save matching restaurants
matches = []
for index, resto in enumerate(restaurantData.restaurant_data):
  resto_type = resto[0]
  if resto_type.startswith(resto_start):
    resto_name = restaurantData.restaurant_data[index][1]
    resto_price = restaurantData.restaurant_data[index][2]
    resto_rating = restaurantData.restaurant_data[index][3]
    resto_address = restaurantData.restaurant_data[index][4]
    matches.append(index)
    print(f"{index:02}. {resto_name} ({resto_type})")
    print(f"\tPrice: {resto_price}/5, Rating = {resto_rating}/5")
    print(f"\tAddress: {resto_address}")
    print()

if(len(matches) > 1):
  print("Our random recommendation for today is:")
  random_index = matches[random.randint(0, len(matches) - 1)]
  resto_type = restaurantData.restaurant_data[random_index][0]
  resto_name = restaurantData.restaurant_data[random_index][1]
  resto_price = restaurantData.restaurant_data[random_index][2]
  resto_rating = restaurantData.restaurant_data[random_index][3]
  resto_address = restaurantData.restaurant_data[random_index][4]
  print(f"{random_index:02}. {resto_name} ({resto_type})")
  print(f"\tPrice: {resto_price}/5, Rating = {resto_rating}/5")
  print(f"\tAddress: {resto_address}")
  print()


print("Thank you for using this program. Have a nice day!")