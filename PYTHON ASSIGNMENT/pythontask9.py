total_seconds = int(input("Enter number of seconds: "))

hours = total_seconds // 3600

remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60 
 
seconds = remaining_seconds % 60

print(total_seconds, "second =", hours, "hour(s),", minutes, "minute(s),", seconds, "second(s)")
