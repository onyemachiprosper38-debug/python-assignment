currentHour = int(input("Enter current hour (0-23): "))

if currentHour <= 11:
    print("Good Morning!!! ")
elif currentHour <= 17:
    print("Good Afternoon!!! ")
elif currentHour <= 21:
    print("Good Eveninng!!! ")
elif currentHour <= 24:
    print("Good Night!!! ")
