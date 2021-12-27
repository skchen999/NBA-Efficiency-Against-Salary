import csv

with open('NBA_Player_Advanced_20-21_raw.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    dics = []
    pre_row = {}
    for row in reader:
        if pre_row and pre_row['Player'] == row['Player']:
        	pre_row['Tm'] = row['Tm']
        else:
        	dics.append(pre_row)
        	pre_row = row
del dics[0]
keys = dics[0].keys()
with open('NBA_Player_Advanced_20-21.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(dics)