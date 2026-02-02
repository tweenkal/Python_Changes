import csv

filename = 'dynamic_data.csv'
fieldnames = ['Country', 'State', 'City']

with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    while True:
        # Ask if user wants to add a new row
        add_row = input('Do you want to add a new entry? (y/n): ').strip().lower()
        if add_row != 'y':
            break

        # Initialize row dictionary
        row = {}

        # Ask for each field
        add_country = input('Do you want to enter Country? (y/n): ').strip().lower()
        if add_country == 'y':
            row['Country'] = input('Enter Country: ').strip()
        else:
            row['Country'] = ''

        add_state = input('Do you want to enter State? (y/n): ').strip().lower()
        if add_state == 'y':
            row['State'] = input('Enter State: ').strip()
        else:
            row['State'] = ''

        add_city = input('Do you want to enter City? (y/n): ').strip().lower()
        if add_city == 'y':
            row['City'] = input('Enter City: ').strip()
        else:
            row['City'] = ''

        # Write the row to CSV
        writer.writerow(row)

print(f'{filename} created successfully with filled data')
