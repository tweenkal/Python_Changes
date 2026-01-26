country_data = {}


def create_data():
    """
    Handles creation of countries, states, and cities.
    """
    # -------- Create Countries --------
    while True:
        country_input = input(
            "\nEnter Country name(s) separated by comma: ").strip()
        if not country_input:
            print("Country cannot be blank")
            continue

        countries_list = [name.strip() for name in country_input.split(",") if
                          name.strip()]

        invalid = [name for name in countries_list if not name.islower()]
        if invalid:
            print("Country names must be all lowercase:", invalid)
            continue

        for name in countries_list:
            if name not in country_data:
                country_data[name] = {}
                print(f"{name} added successfully")
            else:
                print(f"{name} already exists")

        while True:
            choice = input(
                "\nDo you want to enter another country? (Y/N): ").strip()
            if choice in ("Y", "N"):
                break
            print("Please enter only uppercase Y or N")
        if choice == "N":
            break

    print("\nCountry data:", list(country_data.keys()))

    # -------- Create States --------
    while country_data:
        states_input = input(
            "Enter state name(s) separated by comma: ").strip()
        if not states_input:
            print("State cannot be blank")
            continue

        states_list = [name.strip() for name in states_input.split(",") if
                       name.strip()]

        invalid = [name for name in states_list if not name.islower()]
        if invalid:
            print("State names must be all lowercase:", invalid)
            continue

        selected_country = input("Select country for these states: ").strip()
        if selected_country not in country_data:
            print("Invalid country")
            continue

        for state_name in states_list:
            if state_name not in country_data[selected_country]:
                country_data[selected_country][state_name] = []
                print(f"{state_name} added successfully in {selected_country}")
            else:
                print(f"{state_name} already exists in {selected_country}")

        while True:
            choice = input(
                "\nDo you want to enter another state? (Y/N): ").strip()
            if choice in ("Y", "N"):
                break
            print("Please enter only uppercase Y or N")
        if choice == "N":
            break

    print("\nFinal country and states data:")
    for country, states in country_data.items():
        print(f"{country}: {list(states.keys())}")

    # -------- Create Cities --------
    while True:
        print("\nAvailable states by country:")
        for country, states in country_data.items():
            print(f"{country}: {list(states.keys())}")

        cities_input = input(
            "\nEnter city name(s) separated by comma: ").strip()
        if not cities_input:
            print("City cannot be blank")
            continue

        cities_list = [name.strip() for name in cities_input.split(",") if
                       name.strip()]

        invalid = [name for name in cities_list if not name.islower()]
        if invalid:
            print("City names must be all lowercase:", invalid)
            continue

        selected_state = input("Select state for these cities: ").strip()
        state_found = False
        for country in country_data:
            if selected_state in country_data[country]:
                for city_name in cities_list:
                    if city_name not in country_data[country][selected_state]:
                        country_data[country][selected_state].append(city_name)
                        print(
                            f"{city_name} added successfully in {selected_state} ({country})")
                    else:
                        print(
                            f"{city_name} already exists in {selected_state} ({country})")
                state_found = True
                break

        if not state_found:
            print("Invalid state")
            continue

        while True:
            choice = input(
                "\nDo you want to enter another city? (Y/N): ").strip()
            if choice in ("Y", "N"):
                break
            print("Please enter only uppercase Y or N")
        if choice == "N":
            break

    # -------- Final Data --------
    print("\n--- Complete Data ---")
    print(country_data)


def update_data():
    """
    Handles updating country, state, and city names.
    """
    print("\nUpdate Options:")
    print("1. Update Country")
    print("2. Update State")
    print("3. Update City")

    update_choice = int(input("Choose option: "))

    # -------- Update Country --------
    if update_choice == 1:
        print("Countries:", list(country_data.keys()))
        old_country = input("Enter country to update: ")

        if old_country in country_data:
            new_country = input("Enter new country name: ")
            country_data[new_country] = country_data.pop(old_country)

    # -------- Update State --------
    elif update_choice == 2:
        for country, states in country_data.items():
            print(country, ":", list(states.keys()))

        old_state = input("Enter state to update: ")

        for country, states in country_data.items():
            if old_state in states:
                new_state = input("Enter new state name: ")
                states[new_state] = states.pop(old_state)
                break

    # -------- Update City --------
    elif update_choice == 3:
        for country in country_data:
            for state in country_data[country]:
                print(state, ":", country_data[country][state])

        old_city = input("Enter city to update: ")

        for country in country_data:
            for state in country_data[country]:
                if old_city in country_data[country][state]:
                    new_city = input("Enter new city name: ")
                    index = country_data[country][state].index(old_city)
                    country_data[country][state][index] = new_city

    print("\n--- Current Data After Update ---")
    print(country_data)


def delete_data():
    """
    Handles deletion of country, state, and city.
    """
    print("\nDelete Options:")
    print("1. Delete Country")
    print("2. Delete State")
    print("3. Delete City")

    delete_choice = int(input("Choose option: "))

    # -------- Delete Country --------
    if delete_choice == 1:
        print("Countries:", list(country_data.keys()))
        country = input("Enter country to delete: ")
        country_data.pop(country, None)

    # -------- Delete State --------
    elif delete_choice == 2:
        state = input("Enter state to delete: ")
        for country in country_data:
            country_data[country].pop(state, None)

    # -------- Delete City --------
    elif delete_choice == 3:
        city = input("Enter city to delete: ")
        for country in country_data:
            for state in country_data[country]:
                if city in country_data[country][state]:
                    country_data[country][state].remove(city)

    print("\n--- Current Data After Delete ---")
    print(country_data)


# -------------------- MAIN MENU -------------------
while True:
    print("\nMAIN MENU")
    print("1. Create")
    print("2. Update")
    print("3. Delete")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Enter a number from 1 to 4.")
        continue

    if choice == 1:
        create_data()
    elif choice == 2:
        update_data()
    elif choice == 3:
        delete_data()
    elif choice == 4:
        print("Program Ended")
        break
    else:
        print("Invalid choice. Enter 1 to 4.")
