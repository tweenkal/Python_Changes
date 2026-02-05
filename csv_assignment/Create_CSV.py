import csv

filename = 'dynamic_data.csv'
fieldnames = ['Country', 'State', 'City']

countries = {}  # Stores countries, states, and cities

while True:
    print("\nMain Menu")
    print("1. Add Country")
    print("2. Add State")
    print("3. Add City")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    # ---------------- ADD COUNTRY ----------------
    if choice == '1':
        while True:
            country = input("Enter Country name: ").strip()
            if not country:
                print("Country name cannot be empty!")
                continue

            if country in countries:
                print("Country already exists!")
            else:
                countries[country] = {"states": {}}
                print(f"{country} added successfully!")

            another = input("Add another country? (y/n): ").lower()
            if another != 'y':
                break

    # ---------------- ADD STATE ----------------
    elif choice == '2':
        if not countries:
            print("Please add a country first!")
            continue

        while True:
            print("\nAvailable Countries:")
            for index, country in enumerate(countries.keys(), 1):
                print(f"{index}. {country}")

            try:
                c_index = int(input("Select country number: ")) - 1
                country_name = list(countries.keys())[c_index]
            except (ValueError, IndexError):
                print("Invalid selection!")
                continue

            state = input("Enter State name: ").strip()
            if not state:
                print("State name cannot be empty!")
                continue

            if state in countries[country_name]["states"]:
                print("State already exists in this country!")
            else:
                countries[country_name]["states"][state] = []
                print(f"{state} added to {country_name} successfully!")

            another = input("Add another state? (y/n): ").lower()
            if another != 'y':
                break

    # ---------------- ADD CITY ----------------
    elif choice == '3':
        # Check if any state exists
        states_exist = any(countries[c]["states"] for c in countries)
        if not states_exist:
            print("No states available. Add a state first!")
            continue

        while True:
            # Create a list of all states with country info
            all_states = []
            for country, c_data in countries.items():
                for state in c_data["states"]:
                    all_states.append((country, state))

            print("\nAvailable States:")
            for index, (country, state) in enumerate(all_states, 1):
                print(f"{index}. {state} ({country})")

            try:
                s_index = int(input("Select state number: ")) - 1
                country_name, state_name = all_states[s_index]
            except (ValueError, IndexError):
                print("Invalid selection!")
                continue

            city = input(f"Enter City name for {state_name}, {country_name}: ").strip()
            if not city:
                print("City name cannot be empty!")
                continue

            if city in countries[country_name]["states"][state_name]:
                print("City already exists in this state!")
            else:
                countries[country_name]["states"][state_name].append(city)
                print(f"{city} added to {state_name}, {country_name} successfully!")

            another = input("Add another city? (y/n): ").lower()
            if another != 'y':
                break

    elif choice == '4':
        break

    else:
        print("Invalid choice!")

# ---------------- WRITE CSV ----------------
# ---------------- WRITE CSV ----------------
with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for country, c_data in countries.items():
        country_written = False  # Track if country is already written
        for state, cities in c_data["states"].items():
            state_written = False  # Track if state is already written

            if not cities:
                # No cities, just write country and state
                writer.writerow({
                    'Country': country if not country_written else '',
                    'State': state,
                    'City': ''
                })
                country_written = True
            else:
                for city in cities:
                    writer.writerow({
                        'Country': country if not country_written else '',
                        'State': state if not state_written else '',
                        'City': city
                    })
                    country_written = True
                    state_written = True

print(f"\n{filename} created successfully!")
