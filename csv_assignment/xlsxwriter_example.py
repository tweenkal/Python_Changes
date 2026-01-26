import xlsxwriter

# Data to write
data = [
    ['Country', 'State', 'City'],
    ['India', 'Guj', 'Ahmedabad'],
    ['India', 'Guj', 'Gandhinagar'],
    ['India', 'Raj', 'Udaipur'],
    ['India', 'Raj', 'Jodhpur'],
    ['Pak', 'Guj', 'Ahmedabad'],
    ['Pak', 'Guj', 'Gandhinagar'],
    ['Pak', 'Raj', 'Udaipur'],
    ['Pak', 'Raj', 'Jodhpur']
]

workbook = xlsxwriter.Workbook('dynamic_excel.xlsx')
worksheet = workbook.add_worksheet()

for row_idx, row in enumerate(data):
    for col_idx, value in enumerate(row):
        worksheet.write(row_idx, col_idx, value)

workbook.close()
print("dynamic_excel.xlsx created successfully!")
