from datetime import datetime

# Get birthdate from user
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

# Convert input string to date object
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

# Get today's date
today = datetime.today().date()

# Calculate age
age = today.year - birthdate.year
# Adjust if birthday hasn't occurred yet this year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

# Function to check leap year
def is_leap_year(year):
    """
       Check if a given year is a leap year.
       Args:
           year (int): The year to check.
       Returns:
           bool: True if the year is a leap year, False otherwise.
       """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# List all leap years after birth year up to current year
leap_years = [year for year in range(birthdate.year + 1, today.year + 1) if is_leap_year(year)]

# Display results
print(f"Your current age is {age} years.")
print(f"Leap years after your birthdate: {leap_years}")
