# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import cx_Oracle

def opencon():
    con = cx_Oracle.connect('labtec/labtec@127.0.0.1/xe')
    return con



