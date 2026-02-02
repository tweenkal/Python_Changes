import csv

filename = 'dynamic_data.csv'
fieldnames = ['Country', 'State', 'City']

with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    last_country = ''
    last_state = ''

    while True:
        add_row = input('Do you want to add a new entry? (y/n): ').strip().lower()
        if add_row != 'y':
            break

        country = input('Enter Country: ').strip()
        state = input('Enter State: ').strip()

        cities = []
        while True:
            city = input('Enter City (or type "done" to finish this state): ').strip()
            if city.lower() == 'done':
                break
            cities.append(city)

        # Write rows for all cities
        for i, city in enumerate(cities):
            row = {}
            # Only fill country/state if it's different from last written
            if country != last_country:
                row['Country'] = country
                last_country = country
                last_state = ''  # Reset last_state when country changes
            else:
                row['Country'] = ''

            if state != last_state:
                row['State'] = state
                last_state = state
            else:
                row['State'] = ''

            row['City'] = city
            writer.writerow(row)

print(f'{filename} created successfully with filled data.')
