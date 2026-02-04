import csv

filename = 'dynamic_data.csv'
fieldnames = ['Country', 'State', 'City']

# Temporary storage to maintain grouped structure
data = []

while True:
    print("\nMain Menu")
    print("1. Add Country")
    print("2. Add State")
    print("3. Add City")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        while True:
            country = input("Enter Country name: ")
            data.append({'Country': country, 'State': '', 'City': ''})
            another = input("Do you want to add another country? (y/n): ").lower()
            if another != 'y':
                break

    elif choice == '2':
        while True:
            state = input("Enter State name: ")
            country_for_state = input("Enter Country for this State: ")
            data.append({'Country': country_for_state, 'State': state, 'City': ''})
            another = input("Do you want to add another state? (y/n): ").lower()
            if another != 'y':
                break

    elif choice == '3':
        while True:
            city = input("Enter City name: ")
            state_for_city = input("Enter State for this City: ")
            country_for_city = input("Enter Country for this City: ")
            data.append({'Country': country_for_city, 'State': state_for_city, 'City': city})
            another = input("Do you want to add another city? (y/n): ").lower()
            if another != 'y':
                break

    elif choice == '4':
        break
    else:
        print("Invalid choice!")

# Write to CSV with grouped structure
with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    last_country = last_state = ''
    for row in data:
        country_to_write = row['Country'] if row['Country'] != last_country and row['Country'] != '' else ''
        state_to_write = row['State'] if row['State'] != last_state and row['State'] != '' else ''
        writer.writerow({
            'Country': country_to_write,
            'State': state_to_write,
            'City': row['City']
        })
        if row['Country'] != '':
            last_country = row['Country']
        if row['State'] != '':
            last_state = row['State']

print(f"\n{filename} created successfully!")
