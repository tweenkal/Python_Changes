country_data = {}

while True:
    print("\nMAIN MENU")
    print("1. Create")
    print("2. Update")
    print("3. Delete")
    print("4. Exit")

    try:
        main_choice = int(input("Enter your choice: "))
    except:
        print("Invalid input. Enter a number from 1 to 4.")
        continue

    # ---------------- CREATE ----------------
    if main_choice == 1:

        # Create Countries
        while True:
            country_name = input("Enter country name: ").strip()
            if country_name == "":
                print("Country cannot be blank")
                continue

            if country_name not in country_data:
                country_data[country_name] = {}
            else:
                print("Country already exists")

            add_another_country = input("Add another country? (Y/N): ").upper()
            if add_another_country != "Y":
                break

        # Create States
        while country_data:
            state_name = input("Enter state name: ").strip()
            if state_name == "":
                print("State cannot be blank")
                continue

            print("Available Countries:", list(country_data.keys()))
            selected_country = input("Select country for this state: ")

            if selected_country in country_data:
                country_data[selected_country][state_name] = []
            else:
                print("Invalid country")

            add_another_state = input("Add another state? (Y/N): ").upper()
            if add_another_state != "Y":
                break

        # Create Cities
        while True:
            city_name = input("Enter city name: ").strip()
            if city_name == "":
                print("City cannot be blank")
                continue

            print("Available States:")
            for country in country_data:
                for state in country_data[country]:
                    print(f"{state} (Country: {country})")

            selected_state = input("Select state for this city: ")

            all_states = []
            for country in country_data:
                for state in country_data[country]:
                    all_states.append(state)

            if selected_state in all_states:
                for country in country_data:
                    if selected_state in country_data[country]:
                        country_data[country][selected_state].append(city_name)
                        break
            else:
                print("Invalid state")

            add_another_city = input("Add another city? (Y/N): ").upper()
            if add_another_city != "Y":
                break

        # Print data after creation
        print("\n--- Current Data After Create ---")
        print(country_data)

    # ---------------- UPDATE ----------------
    elif main_choice == 2:
        print("\nUpdate Options:")
        print("1. Update Country")
        print("2. Update State")
        print("3. Update City")
        update_choice = int(input("Choose option: "))

        # Update Country
        if update_choice == 1:
            print("Countries:", list(country_data.keys()))
            old_country_name = input("Enter country to update: ")
            if old_country_name in country_data:
                new_country_name = input("Enter new country name: ")
                country_data[new_country_name] = country_data[old_country_name]
                del country_data[old_country_name]

        # Update State
        elif update_choice == 2:
            for country in country_data:
                print(country, ":", list(country_data[country].keys()))
            old_state_name = input("Enter state to update: ")
            for country in country_data:
                if old_state_name in country_data[country]:
                    new_state_name = input("Enter new state name: ")
                    country_data[country][new_state_name] = \
                        country_data[country][old_state_name]
                    del country_data[country][old_state_name]

        # Update City
        elif update_choice == 3:
            for country in country_data:
                for state in country_data[country]:
                    print(state, ":", country_data[country][state])
            old_city_name = input("Enter city to update: ")
            for country in country_data:
                for state in country_data[country]:
                    if old_city_name in country_data[country][state]:
                        new_city_name = input("Enter new city name: ")
                        country_data[country][state].remove(old_city_name)
                        country_data[country][state].append(new_city_name)
                        break

        # Print data after update
        print("\n--- Current Data After Update ---")
        print(country_data)

    # ---------------- DELETE ----------------
    elif main_choice == 3:
        print("\nDelete Options:")
        print("1. Delete Country")
        print("2. Delete State")
        print("3. Delete City")
        delete_choice = int(input("Choose option: "))

        # Delete Country
        if delete_choice == 1:
            print("Countries:", list(country_data.keys()))
            country_to_delete = input("Enter country to delete: ")
            if country_to_delete in country_data:
                del country_data[country_to_delete]

        # Delete State
        elif delete_choice == 2:
            state_to_delete = input("Enter state to delete: ")
            for country in country_data:
                if state_to_delete in country_data[country]:
                    del country_data[country][state_to_delete]

        # Delete City
        elif delete_choice == 3:
            city_to_delete = input("Enter city to delete: ")
            for country in country_data:
                for state in country_data[country]:
                    if city_to_delete in country_data[country][state]:
                        country_data[country][state].remove(city_to_delete)

        # Print data after delete
        print("\n--- Current Data After Delete ---")
        print(country_data)

    # ---------------- EXIT ----------------
    elif main_choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")
