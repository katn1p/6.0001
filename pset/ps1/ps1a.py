currentSavings = 0.00

annualSalary = float(input("Your annual salary: "))
portionSaved = float(input("Portion of salary to be saved (decimal %): "))
totalCost = float(input("Cost of your dream house: "))

monthlySalary = annualSalary / 12
portionDownPayment = 0.25
downPaymentCost = totalCost * portionDownPayment

# End of each month, add portion of salary and the investment's return to savings account. 
month = 0
while currentSavings < downPaymentCost:
    month += 1
    monthlyReturn = (currentSavings * 0.04) / 12
    currentSavings = currentSavings + (monthlySalary * portionSaved) + monthlyReturn
print("Number of months:", month)
