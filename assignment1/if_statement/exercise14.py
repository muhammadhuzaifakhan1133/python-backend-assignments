# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc 
# - RED or red or rEd etc 
# - YELLOW or yellow or yELlOw etc

# program should display the following message on checking above input
# Car is allowed to go
# Car has to wait
# Car has to stop
# invalid input

color = input("Enter signal color: ").capitalize()

if (color == "Green"):
    print("Car is allowed to go")
elif (color == "Yellow"):
    print("Car has to wait")
elif (color == "Red"):
    print("Car has to stop")
else:
    print("Invalid Input")