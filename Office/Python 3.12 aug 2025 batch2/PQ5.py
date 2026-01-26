from datetime import date

birthdate_input = input("Enter your birth date (YYYY-MM-DD): ")
birth_year, birth_month, birth_day = map(int, birthdate_input.split("-"))

birth_date = date(birth_year, birth_month, birth_day)
today = date.today()

# Age calculation
age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

# Days since birth
total_days = (today - birth_date).days

print(f"Your current age is {age} years")
print(f"Total days passed since your birth: {total_days}")
