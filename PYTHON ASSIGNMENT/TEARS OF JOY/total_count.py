total = 0
count = 0

num = int(input("Enter (-1 to stop): "))

while num != -1:
    total = total + num
    count = count + 1
    num = int(input("Enter (-1 to stop): "))

if count == 0:
    print("Count: 0  Average: 0")
else:
    average = total / count
    print("Count:", count, "Average:", average)
