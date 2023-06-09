def main():
    houseCost = 1_000_000
    downPaymentRate = 0.25
    totalCost = houseCost * downPaymentRate

    semiAnnualRaise = 0.07
    annualReturn = 0.04

    annualSalary = float(input("Enter the starting salary: "))
    monthlySalary = annualSalary / 12

    savingsRate, steps = getOptimalSavingsRate(monthlySalary, annualReturn, semiAnnualRaise, totalCost)
    print(f"Best savings rate: {savingsRate}")
    print(f"Steps in bisection search: {steps}")


# Calculates the savings after 36 months, function getOptimalSavingsRate() invokes this function to run through bisection search.
def calcSavingsAfter36Months(monthlySalary, savingsRate, annualReturn, semiAnnualRaise):
    currentSavings = 0
    months = 0
    raiseMonth = 0

    while months < 36:
        months += 1
        raiseMonth += 1

        monthlyReturn = (currentSavings * annualReturn) / 12
        currentSavings = currentSavings + (monthlySalary * savingsRate) + monthlyReturn

        if raiseMonth == 6:
            monthlySalary = monthlySalary + (monthlySalary * semiAnnualRaise)
            raiseMonth = 0

    return currentSavings


# Get the optimal saving rate for every month.
def getOptimalSavingsRate(monthlySalary, annualReturn, semiAnnualRaise, totalCost):
    savingsRate = 0.00
    currentSavings = 0
    epsilon = 100
    low = 0
    high = 10000
    guess = (low + high) // 2
    steps = 0

    while abs(currentSavings - totalCost) >= epsilon:
        steps += 1
        print(guess)
        savingsRate = guess / 10000
        currentSavings = calcSavingsAfter36Months(monthlySalary, savingsRate, annualReturn, semiAnnualRaise) # Calls calcSavingsAfter36Months() with the guess.

        if (currentSavings - totalCost) < 0:
            low = guess
        else:
            high = guess
        guess = (low + high) // 2
        print(savingsRate)
        print(f"{low}, {high}")

    return savingsRate, steps


if __name__ == '__main__':
    main()
