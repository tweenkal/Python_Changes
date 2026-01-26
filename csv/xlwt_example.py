import xlwt

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

book = xlwt.Workbook()
sheet = book.add_sheet('Sheet1')

for row_idx, row in enumerate(data):
    for col_idx, value in enumerate(row):
        sheet.write(row_idx, col_idx, value)

book.save('dynamic_excel_old.xls')
print("dynamic_excel_old.xls created successfully!")
