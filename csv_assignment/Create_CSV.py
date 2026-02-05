import csv

filename = 'dynamic_data.csv'
fieldnames = ['Country', 'State', 'City']

countries = {}  
# Structure will be:
# {
#   "India": {
#       "states": {
#           "Gujarat": ["Ahmedabad", "Surat"],
#           "Maharashtra": ["Mumbai"]
#       }
#   }
# }

while True:
    print("\nMain Menu")
    print("1. Add Country")
    print("2. Add State")
    print("3. Add City")
    print("4. Exit")

    choice = input("Choose an option: ")

    # ---------------- ADD COUNTRY ----------------
    if choice == '1':
        while True:
            country = input("Enter Country name: ").strip()

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
            for i, c in enumerate(countries.keys(), 1):
                print(f"{i}. {c}")

            try:
                c_index = int(input("Select country number: ")) - 1
                country_name = list(countries.keys())[c_index]
            except (ValueError, IndexError):
                print("Invalid selection!")
                continue

            state = input("Enter State name: ").strip()

            if state in countries[country_name]["states"]:
                print("State already exists in this country!")
            else:
                countries[country_name]["states"][state] = []
                print(f"{state} added to {country_name}!")

            another = input("Add another state? (y/n): ").lower()
            if another != 'y':
                break

    # ---------------- ADD CITY ----------------
    elif choice == '3':
        if not countries:
            print("Please add a country and state first!")
            continue

        while True:
            print("\nAvailable Countries:")
            for i, c in enumerate(countries.keys(), 1):
                print(f"{i}. {c}")

            try:
                c_index = int(input("Select country number: ")) - 1
                country_name = list(countries.keys())[c_index]
            except (ValueError, IndexError):
                print("Invalid country selection!")
                continue

            states = countries[country_name]["states"]
            if not states:
                print("No states in this country. Add a state first!")
                continue

            print("\nAvailable States:")
            for i, s in enumerate(states.keys(), 1):
                print(f"{i}. {s}")

            try:
                s_index = int(input("Select state number: ")) - 1
                state_name = list(states.keys())[s_index]
            except (ValueError, IndexError):
                print("Invalid state selection!")
                continue

            city = input("Enter City name: ").strip()

            if city in states[state_name]:
                print("City already exists in this state!")
            else:
                states[state_name].append(city)
                print(f"{city} added to {state_name}, {country_name}!")

            another = input("Add another city? (y/n): ").lower()
            if another != 'y':
                break

    # ---------------- EXIT ----------------
    elif choice == '4':
        break

    else:
        print("Invalid choice!")

# ---------------- WRITE TO CSV ----------------
with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for country, c_data in countries.items():
        writer.writerow({'Country': country, 'State': '', 'City': ''})

        for state, cities in c_data["states"].items():
            writer.writerow({'Country': '', 'State': state, 'City': ''})

            for city in cities:
                writer.writerow({'Country': '', 'State': '', 'City': city})

print(f"\n{filename} created successfully!")
