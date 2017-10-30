import cx_Oracle

con = cx_Oracle.connect('labtec/labtec@127.0.0.1/xe')
print con.version

con.close()
