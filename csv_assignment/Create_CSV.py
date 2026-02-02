import csv

# Output CSV file name
output_csv_file = 'dynamic_data.csv'

# CSV headers
csv_headers = ['Country', 'State', 'City']

# Track current selections
current_country = ''
current_state = ''

# Open CSV for writing
with open(output_csv_file, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()

    while True:
        # Display menu
        print("\nMenu:")
        print("1. Add Country")
        print("2. Add State")
        print("3. Add City")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            current_country = input("Enter Country: ").strip()
            current_state = ''  # Reset state when country changes
            print(f"Country set to '{current_country}'")

        elif choice == '2':
            if not current_country:
                print("Please add a Country first!")
                continue
            current_state = input("Enter State: ").strip()
            print(f"State set to '{current_state}' under Country '{current_country}'")

        elif choice == '3':
            if not current_country:
                print("Please add a Country first!")
                continue
            if not current_state:
                print("Please add a State first!")
                continue

            while True:
                city = input('Enter City: ').strip()
                row_data = {
                    'Country': current_country,
                    'State': current_state,
                    'City': city
                }
                writer.writerow(row_data)
                print(f"City '{city}' added under {current_state}, {current_country}")

                # Ask if user wants to add another city
                add_another = input("Do you want to add another city? (y/n): ").strip().lower()
                if add_another != 'y':
                    break

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

print(f"\n{output_csv_file} created successfully with proper formatting.")
