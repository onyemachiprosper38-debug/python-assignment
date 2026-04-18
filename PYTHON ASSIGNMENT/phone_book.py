while True:
    print("\nMain Menu")
    print("1. Phone Book")
    print("2. Messages")
    print("3. Chat")
    print("4. Call Register")
    print("0. Exit")

    main_choice = int(input("Select: "))

    match main_choice:

      
        case 1:
            print("\nPhone Book")
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
            phone_book = int(input("Select: "))

            match Phone_book:
                case 1:
                    print("Search")
                case 2:
                    print("Service Numbers")
                case 3:
                    print("Add name")
                case 4:
                    print("Erase")
                case 5:
                    print("Edit")
                case 6:
                    print("Assign tone")
                case 7:
                    print("Send b’card")
                case 8:
                    print("\nOptions")
                    print("1. Type of view")
                    print("2. Memory status")
                    print("0. Back")
                    options = int(input("Select: "))
                    match options:
                        case 1:
                            print("Type of view")
                            
                        case 2:
                            print("Memory status")
                            print("0. Back")
                case 9:
                    print("Speed dials")
                    print("0. Back")
                case 10:
                    print("Voice tags")
                    print("0. Back")

       
        case 2:
            print("\nMessages")
            print("1. Write messages")
            print("2. Inbox")
            print("3. Outbox")
            print("4. Picture messages")
            print("5. Templates")
            print("6. Smileys")
            print("7. Message settings")
            print("0. Back")
            msg = int(input("Select: "))

            match Messages:
                case 1:
                    print("Write messages")
                case 2:
                    print("Inbox")
                case 3:
                    print("Outbox")
                case 4:
                    print("Picture messages")
                case 5:
                    print("Templates")
                case 6:
                    print("Smileys")
                case 7:
                    print("\nMessage Settings")
                    print("1. Set 1")
                    print("2. Common")

                    message settings = int(input("Select: "))

                    match message settings:
                        case 1:
                            print("Set 1")
                        case 2:
                            print("Common")
                        case _:
                            print("Invalid")
                case _:
                    print("Invalid")

        
        case 3:
            print("Chat")

        
        case 4:
            print("\nCall Register")
            print("1. Missed calls")
            print("2. Received calls")
            print("3. Dialled numbers")
            print("4. Erase recent call lists")
            print("5. Show call duration")

            cr = int(input("Select: "))

            match cr:
                case 1:
                    print("Missed calls")
                case 2:
                    print("Received calls")
                case 3:
                    print("Dialled numbers")
                case 4:
                    print("Erase lists")
                case 5:
                    print("\nCall Duration")
                    print("1. Last call duration")
                    print("2. All calls duration")
                    print("3. Received calls duration")
                    print("4. Dialled calls duration")
                    print("5. Clear timers")

                    cd = int(input("Select: "))

                    match cd:
                        case 1:
                            print("Last call duration")
                        case 2:
                            print("All calls duration")
                        case 3:
                            print("Received calls duration")
                        case 4:
                            print("Dialled calls duration")
                        case 5:
                            print("Clear timers")
                        case _:
                            print("Invalid")
                case _:
                    print("Invalid")

       
        case 0:
            print("Goodbye!")
            break

        case _:
            print("Invalid choice")
