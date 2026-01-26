import xlwt

# Create an old Excel file (.xls)
book = xlwt.Workbook()
sheet = book.add_sheet('Sheet1')

# Write data
sheet.write(0, 0, 'Name')
sheet.write(0, 1, 'Age')
sheet.write(1, 0, 'Bob')
sheet.write(1, 1, 30)

book.save('example_old.xls')
print("example_old.xls created using xlwt")
