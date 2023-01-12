# Create a calculator that converts hours, minutes, and seconds, to seconds
def to_seconds(hours, minutes, seconds):
    """Converting time to seconds"""
    return hours*3600 + minutes*60 + seconds
print("Welcome to time converter")
# Allow the program to run countless times, until the user exits
replay = "y"
while(replay.lower() == "y"):
    hours = int(input("\nEnter the  number of hours: "))
    minutes = int(input("\nAnd the minutes: "))
    seconds = int(input("\nNow finally the seconds: "))
    # Returning the result
    print("Those are {} seconds".format(to_seconds(hours, minutes, seconds)))
    #Ask if the user wishes to continue/replay
    replay = input("Do you wish to convert again? (Type y to continue)")
print("\nGood bye, enjoy your time 😉")