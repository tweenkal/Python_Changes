from datetime import datetime


def days_until_next_birthday(birthdate_str):
    """Calculate days left until the next birthday."""
    today = datetime.today().date()

    # Convert string to date
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

    # Birthday in the current year
    next_birthday = birthdate.replace(year=today.year)

    # If birthday has already passed this year, take next year
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    # Calculate days left
    days_left = (next_birthday - today).days
    return days_left


def next_leap_year(current_year):
    """Find the next leap year after the given year."""
    year = current_year + 1

    while True:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return year
        year += 1


# ------------------ Main Program ------------------

try:
    birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")

    days_left = days_until_next_birthday(birthdate_input)

    current_year = datetime.today().year
    leap_year = next_leap_year(current_year)

    print(f"Days left until your next birthday: {days_left} days")
    print(f"Next leap year after the current year: {leap_year}")

except ValueError:
    print("❌ Invalid date format. Please enter date as YYYY-MM-DD.")
