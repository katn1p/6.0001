houseCost = 1_000_000
currentSavings = 0
monthsLimit = 36

semiAnnualRaise = 0.07
annualReturn = 0.04

downPaymentRate = 0.25
totalCost = houseCost * downPaymentRate

annualSalary = float(input("Enter the starting salary: "))
monthlySalary = annualSalary / 12


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

def getOptimalSavingsRate(monthlySalary, annualReturn, semiAnnualRaise, totalCost):
    savingsRate = 0.00
    currentSavings = 0
    epsilon = 100
    low = 0
    high = 10000
    guess = (low + high) / 2

    while abs(currentSavings - totalCost) >= epsilon:
        savingsRate = guess / 100.0
        currentSavings = calcSavingsAfter36Months(monthlySalary, savingsRate, annualReturn, semiAnnualRaise)

        if (currentSavings - totalCost) < 0:
            low = guess
        elif (currentSavings - totalCost) > 0:
            high = guess
        else:
            break
        guess = (low + high) / 2

    return savingsRate
