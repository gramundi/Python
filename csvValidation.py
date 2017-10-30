import csv,sys
count=0
numcols=0
numbroke=0
with open('C:\oracle\CSV_DIR\HCOLOCATION_PI.csv', 'r+') as csvOutput:
	data = csv.reader(csvOutput, delimiter=',', quotechar='"')
	try:
		for row in data:
			if count == 0: 
							numcols=len(row) 
							print ("Num Cols",numcols)
			#print row
			#row = row.rstrip('\r\n')
			count=count+1
			if len(row) != numcols:
				numbroke=numbroke+1
				print("row broken: ",count)
	except csv.Error as e:
		sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
print ("numlines--nmbroke",count,numbroke)