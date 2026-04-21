def main_menu():    
    while True:
        print("\nMain Menu")
        print("1. Phone Book")
        print("2. Messages")
        print("3. Chat")
        print("4. Call Register")
        print("5. Tones")
        print("6. Settings")
        print("7. Call divert")
        print("8. Games")
        print("9. Calculator")
        print("10.Reminders")
        print("11. Clock")
        print("12. Profiles")
        print("13. SIM services3")
        print("0. Exit")

        main_choice = input("Select: ")

        match main_choice:
                 case "1": 
                      phone_book()
                 case "2":
                      messages()
                 case "3":
                      chat()
                 case "4":   
                      call_settings()
                 case "5":
                      tones()
                 case "6":
                      sttings()
                 case "7":
                      call_divert()
                 case "8":
                      games()
                 case "9":
                      calculator()
                 case "10":
                     reminders()
                 case "11":
                     clock()
                 case "12":
                     profiles()
                 case "13":
                     sim_services()
                 case "0":
                     break 
main_menu()

def phone_book():
    while True:       
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
            
        choice = input("Select: ")

        match choice:
                case "1":
                    print("Search")
                case "2":
                    print("Service Numbers")
                case "3":
                    print("Add name")
                case "4":
                    print("Erase")
                case "5":
                    print("Edit")
                case "6":
                    print("Assign tone")
                case "7":
                    print("Send b’card")
                case "8":
                    print("\nOptions")
                    print("Type of view")
                    print(" Memory status")
                    print("0. Back")
                case "9":
                    print("Speed dials")
                    print("0. Back")
                case "10":
                    print("Voice tags")
                case "0":
                    break

       
def messages():
    while True:
        print("\nMessages")
        print("1. Write messages")
        print("2. Inbox")
        print("3. Outbox")
        print("4. Picture messages")
        print("5. Templates")
        print("6. Smileys")
        print("7. Message settings")
        print("8. Info service")
        print("9. Voice mailbox number")
        print("10.Service command editor")
        print("0. Back")

        choice = input("Select: ")

        match choice:
                case "1":
                    print("Write messages")
                case "2":
                    print("Inbox")
                case "3":
                    print("Outbox")
                case "4":
                    print("Picture messages")
                case "5":
                    print("Templates")
                case "6":
                    print("Smileys")
                case "7":
                    print("\nMessage Settings")
                    print("1. Set 1")
                    print("2. Common")

        choice = input("Select: ")

        match choice:          
                case "1":
                    print("\nSet 1")
                    print("Message centre number")
                    print("Messages sent as")
                    print("Message validity")
               
                case "2":
                    print("\nCommon")
                    print("Delivery reports")
                    print("Reply via same centre")
                    print("Character support")
                case "0":
                    break
       
def chat():
    while True:
        print("\nChat")
        print("1. Facebook")
        print("0. Back")

        choice = input("select")
             
        match choice:
                case "1":
                    print("\nFacebook")
                    print("Sorry you can't access facebook using NOKIA")
                case "0":
                    break
        
def messages():
    while True:
        print("\nCall Register")
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

        match choice:
                case "1":
                    print("Missed calls")
                case "2":
                    print("Received calls")
                case "3":
                    print("Dialled numbers")
                case "4":
                    print("Erase lists")
                case "5":
                    print("\nCall Duration")
                    print("Last call duration")
                    print("All calls duration")
                    print("Received calls duration")
                    print("Dialled calls duration")
                    print("Clear timers")
                case "6":
                    print("\ncall cost")
                    print("Last call cost")
                    print("All calls’ cost")
                    print("Clear counters")
                case "7":
                    print("\nCall cost settings")
                    print("Call cost limit")
                    print("Show costs in")
                case "8":
                    print("Prepaid credit")
                case "0":
                    break

def chat():
    while True:
        print("\nTones")
        print("1. Ringing tone")
        print("2. Ringing volume")
        print("3. Incoming call alert")
        print("4. Composer")
        print("5. Message alert tone")
        print("6. Keypad tones")
        print("7. Warning and game tones")
        print("8. Vibrating alert")
        print("9. Screen saver")
        print("0. Back")

        choice = input("Select")
    
        match choice:
                case "1":
                    print("Ringing tone activated")
                case "2":
                    print("Ringing tone volume activated")
                case "3":
                    print("Incoming call alert activated") 
        

