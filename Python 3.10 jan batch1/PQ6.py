from datetime import datetime

def calculate_age_simple(birth_year, birth_month, birth_day):
    """Return current age in years based on birthdate."""
    today = datetime.today()
    age = today.year - birth_year

    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1
    return age

def find_leap_years_simple(birth_year):
    """Return list of leap years after birth year up to current year."""
    current_year = datetime.today().year
    leap_years = []

    for year in range(birth_year + 1, current_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years.append(year)

    return leap_years

birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
birth_year, birth_month, birth_day = map(int, birthdate_input.split('-'))

age = calculate_age_simple(birth_year, birth_month, birth_day)
print(f"Your current age is {age} years.")

leap_years = find_leap_years_simple(birth_year)
print(f"Leap years after your birthdate: {leap_years}")
