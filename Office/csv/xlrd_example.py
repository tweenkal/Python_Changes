import xlrd

# Read data from an old Excel file (.xls)
book = xlrd.open_workbook('example_old.xls')  # Make sure this file exists
sheet = book.sheet_by_index(0)

# Print cell values
for row in range(sheet.nrows):
    print(sheet.row_values(row))
