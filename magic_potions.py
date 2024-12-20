# Assignment 6
# In the mystical lands of Pythondale, you've come across a magic potion shop. 
# The shop has a list of potions, and each potion has a set number of ingredients. 
# Your goal is to buy all the ingredients for a specific potion, one ingredient at a time until you have them all.

# Display a list of potions for the user to choose from.
# Ask the user to choose a potion.
# Display the ingredients required for that potion.
# Use a loop to "buy" each ingredient one by one until all ingredients have been purchased.

potions = {
    'Bindweed': ['Aether', 'Quebrith', 'Vermillion'],
    'Kiss': ['Two Vitriols', 'Vermillion'],
    'Thunderbolt': ['Vitriol', 'Rebis', 'Hydragenum' ,'Two Vermillions'],
    'Wolf': ['Two Vitriols', 'Two Hydragenums', 'Vermillion'],
    "Striga's Urge": ['Striga heart', 'Vitriol', 'Aether', 'Hydragenum'],
}

# Display the list of potions
print("Welcome to Pythondale's Magic Potion Shop!")
print("Take a look at the potions we offer:")
for index, potion in enumerate(potions.keys(), 1):
    print(f"{index}. {potion}")


print("")
# Ask the user to choose a potion
choice = int(input("Ennter the corresponding number for the potion you would like to buy ingredients for: "))
selected_potion = list(potions.keys())[choice - 1]
ingredients = potions[selected_potion]
print(f"\nYou chose {selected_potion}. Now, let's buy each ingredient one by one!")


print("")
# Initialize the shopping loop
bought_ingredients = []
index = 0  # Track the ingredient index
while index < len(ingredients):
    # Ask the user if they want to buy the current ingredient
    user_input = input(f"Do you want to buy {ingredients[index]}? (yes/no): ")
    
    if user_input == "yes":
        bought_ingredients.append(ingredients[index])
        print(f"You bought {ingredients[index]}!")
        index += 1
        if len(bought_ingredients) == len(ingredients):
            print(f"\nCongratulations! You bought all the ingredients for {selected_potion}!")
    elif user_input == "no":
        print("You chose to stop shopping.")
        break
    else:
        print("Please answer with 'yes' or 'no'.")