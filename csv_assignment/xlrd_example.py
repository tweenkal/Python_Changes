import xlrd

filename = 'example_old.xls'

try:
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)

    print(f"Data from {filename} (Sheet: {sheet.name}):\n")
    for row_idx in range(sheet.nrows):
        print(sheet.row_values(row_idx))

except FileNotFoundError:
    print(f"{filename} not found. Please create it first using xlwt.")

except xlrd.biffh.XLRDError as e:
    print(f"Error opening {filename}: {e}")
