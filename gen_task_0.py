

intl_format, val = None, "START"
contacts = {"United Kingdom": "+44",
            "Nigeria": "+234",
            "United States": "+1",
            "China": "+86"}
while val != "STOP":
    userphone = input("Enter your local mobile phone number (Digits Only): ")   # e.g. 09034001244
    country = input("Your country please (UK, Nigeria, US or China): ").title() # e.g. Nigeria OR United States
    userphone = userphone[1:]
    if country in contacts.keys():
        intl_format = contacts[country] + userphone
    print(f"International phone format is: {intl_format}")
    val = input("Enter 'STOP' to end the program anytime, hit ENTER key to continue: ").upper()
print("Program Complete!")


