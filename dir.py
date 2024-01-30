#Govind Sharma
#25-March-2023
#deer in headlights program for indecisive eaters

from menu import breakfast, meal, finger_food
import menu
import random
import time 

def select_food():
    category = input("\n\nWhat category of food do you want? \nBreakfast\nMeal\nFinger Food\n>")

    if category == "breakfast" or category == "b":
        breakfast = random.choice(list(menu.breakfast.keys()))
        #time.sleep(1.5)
        print("Your breakfast is", breakfast)
    elif category == "meal" or category == "m" or category == "lunch" or category == "l" or category == "dinner" or category == "d":
        meal = random.choice(list(menu.meal.keys()))
        #time.sleep(1.5)
        print("Your meal is", meal)

    elif category == "snacckies" or category == "snacks" or category == "finger foods" or category == "finger food" or category == "f" or category == "s":
        finger_food = random.choice(list(menu.finger_food.keys()))
        #time.sleep(1.5)
        print("Your snacckies are", finger_food)

    elif category == "quit" or category == "q":
        exit()
    else:
        print("Pardon Garcon!?l")
        
while True:
    select_food()
    time.sleep(2)
    
    
    
    


