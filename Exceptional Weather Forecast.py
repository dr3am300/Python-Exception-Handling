# Objective: 
# The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.
# Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.
# Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. 
# Remember that the formula is (Fahrenheit - 32) * 5/9.
# Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 
# Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.

while True:
    temperature_fahrenheit = input("Please enter the temperature in Fahrenheit: ")
    try:
        temperature_fahrenheit = float(temperature_fahrenheit)
        temperature_celsius = (temperature_fahrenheit - 32) * 5/9
    except ValueError:
        print("Error: Please enter a valid number.")
    else:
        print(f"The temperature {temperature_fahrenheit} Fahrenheit in Celsius is {temperature_celsius:.2f} degrees.")
    finally:
        user_input = input("Would you like to convert another temperature? (yes/no): ")
        if user_input.lower() != "yes":
            break
        
    
    
    
    

    


  