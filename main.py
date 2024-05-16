import os
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

resto_start = input("Please select a restaurant by typing the first several letters of the restaurant name ... ")
print(f"You typed {resto_start} ... processing ...")

print("Here is a list of restaurants that match your search: ")
for index, resto in enumerate(restaurantData.restaurant_data):
  resto_type = resto[0]
  if resto_start in resto_type:
    resto_name = restaurantData.restaurant_data[index][1]
    resto_price = restaurantData.restaurant_data[index][2]
    resto_rating = restaurantData.restaurant_data[index][3]
    resto_address = restaurantData.restaurant_data[index][4]
    print(f"{index:02}. {resto_name} ({resto_type})")
    print(f"Price: {resto_price}/5, Rating = {resto_rating}/5")
    print(f"Address: {resto_address}")
    print()