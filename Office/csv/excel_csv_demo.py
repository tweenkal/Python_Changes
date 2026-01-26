# ================================
# Excel & CSV Demo - Ready to Run
# ================================

import xlsxwriter
import xlwt
import xlrd
import csv
import os

print("=== Python Excel & CSV Demo ===\n")

# --------------------------
# 1. Writing modern Excel (.xlsx) using xlsxwriter
# --------------------------
xlsx_file = 'report.xlsx'
print(f"Creating {xlsx_file}...")

workbook = xlsxwriter.Workbook(xlsx_file)
worksheet = workbook.add_worksheet()

# Headers with bold format
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Name', bold)
worksheet.write('B1', 'Score', bold)

# Sample data
data = [('Alice', 95), ('Bob', 88)]
for i, (name, score) in enumerate(data, start=2):
    worksheet.write(f'A{i}', name)
    worksheet.write(f'B{i}', score)

workbook.close()
print(f"{xlsx_file} created successfully!\n")

# --------------------------
# 2. Writing & Reading legacy Excel (.xls) using xlwt + xlrd
# --------------------------
xls_file = 'legacy_data.xls'
print(f"Creating and reading {xls_file}...")

# Create legacy XLS
book_write = xlwt.Workbook()
sheet_write = book_write.add_sheet('Sheet1')
sheet_write.write(0, 0, 'Name')
sheet_write.write(0, 1, 'Score')

legacy_data = [('Charlie', 78), ('Diana', 85)]
for i, (name, score) in enumerate(legacy_data, start=1):
    sheet_write.write(i, 0, name)
    sheet_write.write(i, 1, score)

book_write.save(xls_file)
print(f"{xls_file} created successfully!")

# Read the same legacy XLS
book_read = xlrd.open_workbook(xls_file)
sheet_read = book_read.sheet_by_index(0)

print(f"Reading data from {xls_file}:")
for row in range(sheet_read.nrows):
    print(sheet_read.row_values(row))
print()

# --------------------------
# 3. Writing and Reading CSV using csv
# --------------------------
csv_file = 'data.csv'
print(f"Creating {csv_file}...")

# Write CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Score'])
    writer.writerow(['Eve', 92])
    writer.writerow(['Frank', 87])

print(f"{csv_file} created successfully!")

# Read CSV
print(f"Reading data from {csv_file}:")
with open(csv_file, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("\n=== All tasks completed successfully! ===")
