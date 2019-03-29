import csv
filename="prathu.csv"
fields = [] 
rows = [] 
with open(filename, 'a') as csvfile: 
	csvreader = csv.reader(csvfile)
	fields = csvreader.next(csvfile) 
	for row in csvreader: 
		rows.append(row) 
print("Total no. of rows: %d"%(csvreader.line_num)) 