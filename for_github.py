import xlrd
import pprint
import numpy

wd = xlrd.open_workbook('pca_data_all(fish13+回転角度(absなし)+加速度再計算).xlsx')

sheets = wd.sheets()

sheet = wd.sheet_by_name('Sheet1')

pprint.pprint([sheet.row_values(x) for x in range(3)])
pprint.pprint([sheet.col_values(x) for x in range(3)])

length = sheet.nrows
print(length)
a = [sheet.row_values(x) for x in range(length)]
