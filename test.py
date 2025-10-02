import numpy as np

def userInput(prompt):
    while True:
        choice = list(map(int, input(prompt).split()))
        if not choice:
            print("No input received.")
        else:
            return choice

def balanceOption(constraints, materials):
    A = np.array(materials)
    inv_A = np.linalg.inv(A)
    b = np.array(constraints)
    x = np.linalg.inv(A).dot(b)

def soloOption():
    
                
def main():
    print("Please enter each value with a space between all the numbers")
    constraints = userInput("Constraints: ")
    profits = userInput("Profits: ")
    materials = []
    for i in range(3):
        print(f"Enter the materials required for the {i+1}th unit.")
        materials.append(userInput("Materials: "))

    
main()
