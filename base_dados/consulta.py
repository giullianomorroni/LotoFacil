'''
Created on 14/08/2012

@author: giulliano
'''

from sqlite3 import dbapi2 as sqlite

class consulta(object):

    global database;

    def __init__(self):
        #database = '/Development/sqlite/lotofacil';
        database = '/opt/lotofacil/sqlite/lotofacil'
        self.con = sqlite.connect(database)

    def consulta_ano_mes(self, mes=1, ano=1990):
        r = self.con.execute('select bola_1, bola_2, bola_3,' + 
        ' bola_4, bola_5, bola_6, bola_7, bola_8, bola_9, bola_10, bola_11, bola_12, bola_13, ' + 
        ' bola_14, bola_15 from loto where ano >= %d and mes >= %d ' % (ano, mes))
        return r
