import csv

data = [
    {'Country': 'India', 'State': 'Guj', 'City': 'Ahmedabad'},
    {'Country': 'India', 'State': 'Guj', 'City': 'Gandhinagar'},
    {'Country': 'India', 'State': 'Raj', 'City': 'Udaipur'},
    {'Country': 'India', 'State': 'Raj', 'City': 'Jodhpur'},
    {'Country': 'Pak', 'State': 'Guj', 'City': 'Ahmedabad'},
    {'Country': 'Pak', 'State': 'Guj', 'City': 'Gandhinagar'},
    {'Country': 'Pak', 'State': 'Raj', 'City': 'Udaipur'},
    {'Country': 'Pak', 'State': 'Raj', 'City': 'Jodhpur'}
]

filename = 'dynamic_data.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Country', 'State', 'City'])
    writer.writeheader()
    writer.writerows(data)

print(f"{filename} created successfully with filled data")
