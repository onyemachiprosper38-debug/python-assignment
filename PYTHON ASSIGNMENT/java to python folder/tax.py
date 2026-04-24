monthly_salary = int(input("Enter monthly salary: "))

anual_salary = monthly_salary * 12
tax = 0
annual_salary = 0
taxable_amount = 0
first_tax = 0
remaining = 0
second_tax = 0
if (annual_salary <= 300000):
    tax = 0

elif (annual_salary <= 600000):

    taxable_amount = annual_salary - 300000

tax = taxable_amount * 0.15

if (first_tax == 45000):

    remaining = annual_salary - 600000

second_tax = remaining * 0.25

tax = first_tax + second_tax

print("Annual Salary is: " , annual_salary)

print("Tax to pay is: ", tax)
                                                                             

