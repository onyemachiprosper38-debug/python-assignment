hour = int(input("Enter hour: "))

minutes = int(input("Enter minutes: "))

hour_two = int(input("Enter hour: "))

minutes_two = int(input("Enter minutes:"))

print(hour, minutes)

print(hour_two, minutes_two)

final_hour = hour + hour_two

final_minutes = minutes + minutes_two

if (final_minutes >= 60):
        final_minutes += final_minutes // 60
        final_hour = final_hour % 60

elif (final_hour <= 12):
        final_hour = final_hour - 1  
print(f"the time is: {final_hour}: {final_minutes:02d}")               
