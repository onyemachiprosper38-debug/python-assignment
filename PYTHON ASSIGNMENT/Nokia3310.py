def main_menu():
    while True:
        print("\n=== NOKIA MENU ===")
        print("1. Phone book")
        print("2. Messages")
        print("3. Chat")
        print("4. Call register")
        print("0. Exit")

        choice = input("Select: ")

        if choice == "1":
            phone_book()
        elif choice == "2":
            messages()
        elif choice == "3":
            print("Chat feature not implemented.")
        elif choice == "4":
            call_register()
        elif choice == "0":
            print("Goodbye!")
            break
def phone_book():
    while True:
        print("\n--- Phone Book ---")
        print("1. Search")
        print("2. Service Nos.")
        print("3. Add name")
        print("4. Erase")
        print("5. Edit")
        print("6. Assign tone")
        print("7. Send b’card")
        print("8. Options")
        print("9. Speed dials")
        print("10. Voice tags")
        print("0. Back")

        choice = input("Select: ")

        if choice == "8":
            phonebook_options()
        elif choice == "0":
            break
        else:
            print("Feature not implemented yet.")


def phonebook_options():
    while True:
        print("\n--- Phone Book Options ---")
        print("1. Type of view")
        print("2. Memory status")
        print("0. Back")

        choice = input("Select: ")
        if choice == "0":
            break


def messages():
    while True:
        print("\n--- Messages ---")
        print("1. Write messages")
        print("2. Inbox")
        print("3. Outbox")
        print("4. Picture messages")
        print("5. Templates")
        print("6. Smileys")
        print("7. Message settings")
        print("8. Info service")
        print("9. Voice mailbox number")
        print("10. Service command editor")
        print("0. Back")

        choice = input("Select: ")

        if choice == "7":
            message_settings()
        elif choice == "0":
            break
        else:
            print("Feature not implemented yet.")


def message_settings():
    while True:
        print("\n--- Message Settings ---")
        print("1. Set 1")
        print("2. Common")
        print("0. Back")

        choice = input("Select: ")

        if choice == "1":
            set1()
        elif choice == "2":
            common_settings()
        elif choice == "0":
            break


def set1():
    while True:
        print("\n--- Set 1 ---")
        print("1. Message centre number")
        print("2. Messages sent as")
        print("3. Message validity")
        print("0. Back")

        if input("Select: ") == "0":
            break


def common_settings():
    while True:
        print("\n--- Common Settings ---")
        print("1. Delivery reports")
        print("2. Reply via same centre")
        print("3. Character support")
        print("0. Back")

        if input("Select: ") == "0":
            break


def call_register():
    while True:
        print("\n--- Call Register ---")
        print("1. Missed calls")
        print("2. Received calls")
        print("3. Dialled numbers")
        print("4. Erase recent call lists")
        print("5. Show call duration")
        print("6. Show call costs")
        print("7. Call cost settings")
        print("8. Prepaid credit")
        print("0. Back")

        choice = input("Select: ")

        if choice == "5":
            call_duration()
        elif choice == "6":
            call_costs()
        elif choice == "7":
            call_cost_settings()
        elif choice == "0":
            break


def call_duration():
    while True:
        print("\n--- Call Duration ---")
        print("1. Last call duration")
        print("2. All calls duration")
        print("3. Received calls duration")
        print("4. Dialled calls duration")
        print("5. Clear timers")
        print("0. Back")

        if input("Select: ") == "0":
            break


def call_costs():
    while True:
        print("\n--- Call Costs ---")
        print("1. Last call cost")
        print("2. All calls cost")
        print("3. Clear counters")
        print("0. Back")

        if input("Select: ") == "0":
            break


def call_cost_settings():
    while True:
        print("\n--- Call Cost Settings ---")
        print("1. Call cost limit")
        print("2. Show costs in")
        print("0. Back")

        if input("Select: ") == "0":
            break




if __name__ == "__main__":
    main_menu()
