weight = float(input("Enter weight (in kg) "))
height = float(input("Enter Height (in meters) "))
bmi = weight / (height * height)
print(bmi)
if bmi < 18.5:
print("You are underweight ")
elif bmi >= 18.5 and bmi <= 24.9:
print("Your weight is normal ")
elif bmi >= 25 and bmi <= 29.9:
print("You are overweight ")
elif bmi >= 30:
print("obese ")
