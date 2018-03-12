import pandas as pd
import csv

# fh = open('data.csv')  # second argument: default "read"
# all_id = []
# reader = csv.reader(fh, delimiter=',')
#
# for record in reader:     # loop through each row
#     all_id.append(record[1])
#
# for record2 in reader:
#     if record2[1] is in all_id
writer = pd.ExcelWriter('output.xlsx')
output_file = open('output.txt','w')
df = pd.read_excel('data.xlsx', sheetname='NWF Data for Enjoy The Journey ')

ids = df['Membershi UUID']
# print(ids)

x = df[ids.isin(ids[ids.duplicated()])]
x.to_excel(writer, 'sheet1')

# print(x)


# print(y)
# fh = open(y)
# reader = csv.reader(y)
# for record in reader:
#     print(record)


# output_file.write(y)
