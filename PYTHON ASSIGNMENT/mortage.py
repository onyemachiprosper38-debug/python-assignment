print("Welcome to Mortgage Calculator")

principal = float(input("Enter the loan amount: "))

rate = float(input("Enter the annual interest rate (%): "))

years = int(input("Enter the duration in years: "))


monthly_rate = rate / 100 / 12
months = years * 12


monthly_payment = principal * (
    monthly_rate * (1 + monthly_rate) ** months
) / (
    (1 + monthly_rate) ** months - 1
)


print("Your monthly payment is:", round(monthly_payment, 2))
