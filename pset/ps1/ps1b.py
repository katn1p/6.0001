currentSavings = 0.00

annualSalary = float(input("Your annual salary: "))
portionSaved = float(input("Portion of salary to be saved (decimal %): "))
houseCost = float(input("Cost of your dream house: "))
semiAnnualRaise = float(input("semi-annual raise (decimal %): "))

monthlySalary = annualSalary / 12
downPaymentRate = 0.25
totalCost = houseCost * downPaymentRate

# Every 6 months, raise monthly salary.
months = 0
raiseMonth = 0
while currentSavings < totalCost:
    months += 1
    raiseMonth += 1
    monthlyReturn = (currentSavings * 0.04) / 12
    currentSavings = currentSavings + (monthlySalary * portionSaved) + monthlyReturn

    if raiseMonth == 6:
        monthlySalary = monthlySalary + (monthlySalary * semiAnnualRaise) 
        raiseMonth = 0
print(f"Number of months: {months}")
