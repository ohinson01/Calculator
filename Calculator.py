'''
Program: Write a Calculator
Date: 5/19/2020

Maintenance History:
    5/19/2020 - Create program
'''
#Create function to add two numbers
def add (num1, num2):
    return num1 + num2

#Create function to subtract two numbers
def subtract (num1, num2):
    return num1 - num2
'''
Program prompts user to add, subtract or quit
Action executed depending on user prompt
'''
#Create code to ask user input and repeat until prompted to end progrma 
option = input("Do you want to add, subtract or quit program? \nType add, subtract or quit: ")
while option != 'quit':
    try:
        #Execture action based on option input by user
        if option == 'quit':
            break
        elif option == 'add':
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            print(num1, " + ", num2, "= ", add(num1, num2))
            print() #print blank line
        elif option == 'subtract':
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            print(num1, " - ", num2, "= ", subtract(num1, num2))
            print() #print blank line
        else:
            print("You entered an invalid option. Please try again.\n")
    except ValueError:
        print("You did not entere a number. Please try again.\n")
    option = input("Do you want to run the program again?\nType add, subtract or quit: ")
print("\nThank you for using the calculator.")

    
    
    
                 
    
