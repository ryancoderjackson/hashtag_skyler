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


# While Loop
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


# For Loop
choose = input("Which potion would you like to buy? ")
choice = choose
if choice == "Bindweed" or choice == "bindweed":
    print(f"The ingredients for Bindweed are:")
    for bindweed in potions['Bindweed']:
        print(bindweed)
    print("")
    print("Let's buy each ingredient one by one.")
    print("")
    for aether in potions['Bindweed']:
        buy = input(f"Would you like to buy {aether}? (yes/no): ")
        if buy == "yes":
             print(f"You just bought {aether}!")
        elif buy == "no":
            print("You chose to stop shopping. We hope that you visit Pythondale's Magic Potion Shop again.")
            break
        else:
             print("I'm sorry. Please choose yes or no.")
        print("")
        if buy == "yes":
            print("You bought all the ingredients to Bindweed!")
elif choice == "Kiss" or choice == "kiss":
    print(f"The ingredients for Kiss are:")
    for kiss in potions['Kiss']:
        print(kiss)
        print("")
    print("Let's buy each ingredient one by one.")
    print("")
    for vermillion in potions["Kiss"]:
        buy = input(f"Would you like to buy {vermillion}? (yes/no): ")
        if buy == "yes":
            print(f"You just bought {vermillion}!")
        elif buy == "no":
            print("You chose to stop shopping. We hope that you visit Pythondale's Magic Potion Shop again.")
            break
        else:
            print("I'm sorry. Please choose yes or no.")
        print("")
        if buy == "yes":
            print("You bought all the ingredients to Kiss!")
elif choice == "Thunderbolt" or choice == "thunderbolt":
    print(f"The ingredients for Thunderbolt are:")
    for thunderbolt in potions['Thunderbolt']:
        print(thunderbolt)
    print("")
    print("Let's buy each ingredient one by one.")
    print("")
    for vitriol in potions['Thunderbolt']:
        buy = input(f"Would you like to buy {vitriol}? (yes/no): ")
        if buy == "yes":
            print(f"You just bought {vitriol}!")
        elif buy == "no":
            print("You chose to stop shopping. We hope that you visit Pythondale's Magic Potion Shop again.")
            break
        else:
            print("I'm sorry. Please choose yes or no.")
        print("")
        if buy == "yes":
            print("You bought all the ingredients to Thunderbolt!")
elif choice == "Wolf" or choice == "wolf":
    print(f"The ingredients for Wolf are:")
    for wolf in potions['Wolf']:
        print(wolf)
    print("")
    print("Let's buy each ingredient one by one.")
    print("")
    for hydragenum in potions['Wolf']:
        buy = input(f"Would you like to buy {hydragenum}? (yes/no): ")
        if buy == "yes":
            print(f"You just bought {hydragenum}!")
        elif buy == "no":
            print("You chose to stop shopping. We hope that you visit Pythondale's Magic Potion Shop again.")
            break
        else:
            print("I'm sorry. Please choose yes or no.")
        print("")
        if buy == "yes":
            print("You bought all the ingredients to Wolf!")
elif choice == "Striga's Urge" or choice == "striga's urge":
    print(f"The ingredients for Striga's Urge are:")
    for striga in potions["Striga's Urge"]:
        print(striga)
    print("")
    print("Let's buy each ingredient one by one.")
    print("")
    for urge in potions["Striga's Urge"]:
        buy = input(f"Would you like to buy {urge}? (yes/no): ")
        if buy == "yes":
             print(f"You just bought {urge}!")
        elif buy == "no":
            print("You chose to stop shopping. We hope that you visit Pythondale's Magic Potion Shop again.")
            break
        else:
            print("I'm sorry. Please choose yes or no.")
        print("")
        if buy == "yes":
            print("You bought all the ingredients to Striga's Urge!")
else:
    print("I'm sorry we don't carry that potion here at Pythondale's Magic Potion Shop.")
print("Thank you for shopping at Pythondale's Magic Potion Shop. Have a great day!")