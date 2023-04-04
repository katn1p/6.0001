currentSavings = 0.00

annualSalary = float(input("Your annual salary: "))
portionSaved = float(input("Portion of salary to be saved (decimal %): "))
houseCost = float(input("Cost of your dream house: "))

monthlySalary = annualSalary / 12
downPaymentRate = 0.25
totalCost = houseCost * downPaymentRate

months = 0
while currentSavings < totalCost:
    months += 1
    monthlyReturn = (currentSavings * 0.04) / 12
    currentSavings = currentSavings + (monthlySalary * portionSaved) + monthlyReturn
print(f"Number of months: {months}")
