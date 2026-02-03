import csv

filename = 'dynamic_data.csv'
fieldnames = ['Country', 'State', 'City']

with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    while True:  # COUNTRY LEVEL
        print("\n1. Add Country")
        print("2. Finish and Save")
        choice_country = input("Choose an option: ")

        if choice_country == '2':
            break
        elif choice_country != '1':
            print("Invalid choice!")
            continue

        country = input("Enter Country name: ")
        first_state_for_country = True  # Track first state

        while True:  # STATE LEVEL
            print(f"\n--- Country: {country} ---")
            print("1. Add State")
            print("2. Go Back to Country Menu")
            choice_state = input("Choose an option: ")

            if choice_state == '2':
                break
            elif choice_state != '1':
                print("Invalid choice!")
                continue

            state = input("Enter State name: ")
            first_city_for_state = True  # Track first city

            while True:  # CITY LEVEL
                print(f"\n--- State: {state} ({country}) ---")
                print("1. Add City")
                print("2. Go Back to State Menu")
                choice_city = input("Choose an option: ")

                if choice_city == '2':
                    break
                elif choice_city != '1':
                    print("Invalid choice!")
                    continue

                city = input("Enter City name: ")

                writer.writerow({
                    'Country': country if first_state_for_country and first_city_for_state else '',
                    'State': state if first_city_for_state else '',
                    'City': city
                })

                first_state_for_country = False
                first_city_for_state = False

                print("✅ City added!")

print(f"\n🎉 {filename} created successfully with grouped structure!")
