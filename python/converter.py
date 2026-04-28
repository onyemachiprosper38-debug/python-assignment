def convert_usd_to_naira(dollars):
    rate = 1550
    naira = dollars * rate
    return naira

usd = float(input("Enter amount in dollars: "))

naira = convert_usd_to_naira(usd)
print("Amount in naira is:", naira, "Naira ")


