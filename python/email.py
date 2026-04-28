def is_valid_email(email):

    
    valid = True

    
    if len(email) < 8:
        valid = False

    
    if "@" not in email:
        valid = False

    
    if email.startswith("@"):
        valid = False

    
    if email.endswith("@"):
        valid = False

    return valid



email = input("Enter your email: ")

if is_valid_email(email):
    print("Email is valid")
else:
    print("Email is invalid")
