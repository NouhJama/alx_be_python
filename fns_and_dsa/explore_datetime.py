from datetime import timedelta, datetime

def display_current_datetime():
    # Display the current date and time in a readable format
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()

def calculate_future_date(days_ahead):
    # Calculate the date a certain number of days from today
    future_date = datetime.now() + timedelta(days=days_ahead)
    return future_date.strftime("%Y-%m-%d") 

days = int(input("Enter number of days to add to the current date: "))
future_date = calculate_future_date(days)
print("Future date:", future_date)