#Week7 Python User Input and While Loops - Student: Ryan Collier
pizza_orders = ['Cheese', 'Pepporoni','Meat Lovers', 'Greek', 'Deep Dish']
finished_pizzas = []

#Goal Number 1: Loop through pizza orders and print message saying "Your pizza pie is finished"
#Note: ReadMe does not state to print the individual pizza name - thus accomplishes the task for 5 pizzas
while pizza_orders:
    current_pizza = pizza_orders.pop()
    print("Your pizza pie is finished!")
    finished_pizzas.append(current_pizza)

#Goal Number 2: After all Pizzas were made, print "The pizza {name} was made for each pizza"
#Note: Two lists utilized with pop command, reverting the order back to original and printing
while finished_pizzas:
    current_pizza = finished_pizzas.pop()
    print (f"The pizza {current_pizza} was made.")
    

