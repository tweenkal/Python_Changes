import xlsxwriter

# Create a new Excel file (.xlsx)
workbook = xlsxwriter.Workbook('example.xlsx')
worksheet = workbook.add_worksheet()

# Write data
worksheet.write('A1', 'Name')
worksheet.write('B1', 'Age')
worksheet.write('A2', 'Alice')
worksheet.write('B2', 25)

workbook.close()
print("example.xlsx created using xlsxwriter")
