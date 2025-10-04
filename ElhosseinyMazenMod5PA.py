import numpy as np

def userInputHelper(prompt):    # Helper function to put all user data in a list
    while True:
        choice = list(map(float, input(prompt).split()))
        if not choice:
            print("No input received.")
        else:
            return choice

def userInputVariable(prompt):  # helper function to accept a numerical value for variables/constraints
    while True:
        choice = input(prompt)
        if not choice:
            print("No input received.")
        else:
            try:
                choice_int = int(choice)
                if choice_int >= 1:
                    return choice_int
                else:
                    print("Value has to be greater than or equal to 1.")
            except ValueError:
                print("Invalid input.")

def userInput():    # Takes user input
    print("Please enter each value with a space between all the numbers")
    n = userInputVariable("Enter the numbers of variables/constraints (2 for a 2x2, or 3 for 3x3): ")
    coefficients = userInputHelper("Enter the coefficients for each variable for the objective function: ")
    constraints = userInputHelper("Enter a limit for each constraint: ")
    materials = []
    print(f"Enter {n} values to match the variables/constraints to make 1 unit of said product: ")
    for i in range(n):
        materials.append(userInputHelper(f"Enter the values required for the {i + 1}th product: "))
    return n, coefficients, constraints, materials

def balanceOption(constraints, materials):  # Calculates balance option
    A = np.array(materials)
    b = np.array(constraints)
    x = np.linalg.inv(A).dot(b)
    return x

def balancedOptionArray(n, materials):  # getting appropriate array format for balance option calculation
    balancedArray = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            balancedArray[j][i] = materials[i][j]
    return balancedArray

def soloOption(constraint, material):   # calculates the solo option units to produce
    potentialMins = []
    for i in range(len(constraint)):
        if material[i] > 0:
            potentialMins.append(constraint[i]/material[i])
    minNum = min(potentialMins)
    return minNum

def findSum(coefficients, option):  # finds the sum depending on the option that is put in
    sum = 0
    for i in range(len(coefficients)):
        sum += coefficients[i] * option[i]
    return sum

def soloAndSum(n, coefficients, constraints, materials):    # gets the solo options and returns the sum of them
    solos = []
    for i in range(n):
        new = [0] * n
        new[i] = soloOption(constraints, materials[i])
        solos.append(new)
    soloSums = []
    for row in solos:
        soloSums.append(findSum(coefficients, row))
    return solos, soloSums

# best solution
def bestSolution(solutions):    # find the best solution
    bestSolution = 0
    bestSolutionName = ""
    for key, value in solutions.items():
        if value > bestSolution:
            bestSolution = value
            bestSolutionName = key
    return bestSolution, bestSolutionName

def main():
    n, coefficients, constraints, materials = userInput()   # getting all values from the user
    balancedArray = balancedOptionArray(n, materials)   # formating the materials for the balance option function
    solos, soloSums = soloAndSum(n, coefficients, constraints, materials)   # getting all solo units and values
    balance = balanceOption(constraints, balancedArray) #getting balanced option and sum
    balanceSum = findSum(coefficients, balance)

    solutions = {}   #putting all solutions in dictionary
    for i in range(n):
        solutions[f"Solo Solution {i}"] = soloSums[i]
    solutions["Balanced Solution"] = balanceSum

    finalSolution, finalSolutionName = bestSolution(solutions)  # finding the best solution

    #print Statement
    firstRow = ["SUPPLY"]
    for i in range(n):
        firstRow.append(f"CONSTRAINT {i+1}")
    firstRow.append("PROFIT")
    print(firstRow)
    for i in range(n):
        print(f"VARIABLE {i}:", materials[i], coefficients[i])
    print("AVAILABILITY:", constraints)
    for i in range(n):
        print(f"If only Variable {i} is made, there would be a profit of: ${soloSums[i]}. The number of units produced would be", solos[i])
    print(f"The balanced amount is : ${balanceSum}. The breakdown is: {balance} of each of the {n} variables.")
    print(f"The best possible solution is ${finalSolution} using the {finalSolutionName}.")

main()

# Please enter each value with a space between all the numbers
# Enter the numbers of variables/constraints (2 for a 2x2, or 3 for 3x3): 2
# Enter the coefficients for each variable for the objective function: 50 40
# Enter a limit for each constraint: 750 1000
# Enter 2 values to match the variables/constraints to make 1 unit of said product:
# Enter the values required for the 1th product: 1 2
# Enter the values required for the 2th product: 1.5 1
# ['SUPPLY', 'CONSTRAINT 1', 'CONSTRAINT 2', 'PROFIT']
# VARIABLE 0: [1.0, 2.0] 50.0
# VARIABLE 1: [1.5, 1.0] 40.0
# AVAILABILITY: [750.0, 1000.0]
# If only Variable 0 is made, there would be a profit of: 25000.0. The number of units produced would be [500.0, 0]
# If only Variable 1 is made, there would be a profit of: 20000.0. The number of units produced would be [0, 500.0]
# The balanced amount is: 28750.0. The breakdown is: [375. 250.] of each of the 2 variables.
# The best possible solution is 28750.0 using the Balanced Solution.