largest = None

while True:
    user_input = input("Enter: ")

    if user_input == "done":
        break

    num = int(user_input)

    if largest is None:
        largest = num
    elif num > largest:
        largest = num

print("Largest:", largest)

