# Module to  simulate the GDDB Interface and give teh csv output with the operation to perform over the IMPACT DB
# 
# 
import cx_Oracle
from oracle_conn import opencon

import csv,sys
num_upds=0;
num_ins=0;
#Scan the file 
with open('C:\oracle\CSV_DIR\GDDB_PERSONNEL_20170328131530.csv', 'r+') as csvInp,open('C:\oracle\CSV_DIR\GDDB_PERSONNEL_20170328131530GG.csv', 'w+') as csvOut:
        data = csv.reader(csvInp, delimiter=',', quotechar='"')
        csvreader = csv.DictReader(csvInp)
        fieldnames = ['Operation'] + csvreader.fieldnames
        dataw = csv.DictWriter(csvOut, fieldnames,delimiter=',',lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
        headers = {} 
        for n in dataw.fieldnames:
            headers[n] = n
        dataw.writerow(headers)
	try:
            #skip the first row which is the header
            rownum=0
            connection = opencon()
            for row in csvreader:
			#open connection
                        print 'rownum-->'+str(csvreader.line_num)
                        cur=connection.cursor() 
                        ##print row[4] index of the data you want to check
                        #res = cur.callfunc('search_row',cx_Oracle.NUMBER,(row[4],'EMPLOYEE','EMP_NAME'))
                        print 'Check on UNIQUE_ID:'+row['UNIQUE_ID']
                        res = cur.callfunc('search_row',cx_Oracle.NUMBER,(row['UNIQUE_ID'],'personnel','USERNAME'))
                        if res: 
                            #print 'UPDATE--->'
                            num_upds=num_upds+1
                            row['Operation']='UPDATE'
                            dataw.writerow(row)
                        else:
                            print 'Check on OBJECT_ID:'+row['OBJECT_ID']
                            res = cur.callfunc('search_row',cx_Oracle.NUMBER,(row['OBJECT_ID'],'personnel','MY_TRIALS_USERNAME'))
                            if res:
                               #print 'UPDATE--->'
                               num_upds=num_upds+1
                               row['Operation']='UPDATE'
                               dataw.writerow(row)
                            else:
                               #print 'INSERT--->'
                               num_ins=num_ins+1
                               row['Operation']='INSERT'
                               dataw.writerow(row)
                        rownum=rownum+1       
	except csv.Error as e:
		sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
        cur.close()
        connection.close()
print 'num# UPDATES='+str(num_upds)+' num# INSERT='+str(num_ins)
 
