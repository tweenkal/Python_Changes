import csv

# File name
csv_filename = 'dynamic_data.csv'

# CSV headers (use proper capitalization)
csv_headers = ['Country', 'State', 'City']

with open(csv_filename, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()

    last_country = ''
    last_state = ''

    while True:
        add_entry = input('Do you want to add a new entry? (y/n): ').strip().lower()
        if add_entry != 'y':
            break

        # Get country and state
        country = input('Enter Country: ').strip()
        state = input('Enter State: ').strip()

        # Get multiple cities for this state
        cities = []
        while True:
            city = input('Enter City (or type "done" to finish this state): ').strip()
            if city.lower() == 'done':
                break
            cities.append(city)

        # Write each city as a row, leaving country/state blank if repeated
        for i, city in enumerate(cities):
            row_data = {}
            # Only write country if it's different from last
            if country != last_country:
                row_data['Country'] = country
                last_country = country
                last_state = ''  # Reset last_state when country changes
            else:
                row_data['Country'] = ''

            # Only write state if it's different from last
            if state != last_state:
                row_data['State'] = state
                last_state = state
            else:
                row_data['State'] = ''

            row_data['City'] = city
            writer.writerow(row_data)

print(f'{csv_filename} created successfully with proper formatting.')
