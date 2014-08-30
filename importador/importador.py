# -*- coding: utf-8 -*-
import sys
import os
from sqlite3 import dbapi2 as sqlite
from collections import deque
from bs4 import BeautifulSoup

#Esta classe serve para ler o resultado e armazenar na base
class importador:

    global database;
    global repeticoesNumero;

    def __init__(self):
        #database = '/Development/sqlite/lotofacil';
        database = '/opt/lotofacil/sqlite/lotofacil'
        self.con = sqlite.connect(database)
        
    def commit(self):
        self.con.commit()

    def apagar_tabela(self):
        try:
            os.remove(database)
        except Exception:
            print ('A tabela nao existe')      

    def criar_tabela(self):
        self.con.execute(
                         ' create table loto (concurso, dia, mes, ano, bola_1, bola_2, bola_3,' + 
                         ' bola_4, bola_5, bola_6, bola_7, bola_8, bola_9, bola_10, bola_11, bola_12, bola_13, ' + 
                         ' bola_14, bola_15, ganhadores_15, ganhadores_14, ganhadores_13, ganhadores_12, ganhadores_11)')

    def popular_base(self):
        soup = BeautifulSoup(open("D_LOTFAC.HTM"))
        table = soup.table;
        trs = table.find_all('tr')
        r = []

        #nao esta funcionando
        
        for tr in trs:
            tds = tr.find_all('td')
            for td in tds:
                print(td.contents[0])
                r.append(td.contents[0])

            print(r)
            concurso = r[0]
            data = r[1]
            dia = data.split('/')[0]
            mes = data.split('/')[1]
            ano = data.split('/')[2]
            ganhadores_15 = r[18]
            ganhadores_14 = r[19]
            ganhadores_13 = r[20]
            ganhadores_12 = r[21]
            ganhadores_11 = r[22]

            bolas_ordenadas = deque();
            for bola in range(2, 17):
                bolas_ordenadas.append(int(r[bola]))
            bo = sorted(bolas_ordenadas)

            self.con.execute('insert into loto (concurso, dia, mes, ano, bola_1, bola_2, bola_3,' + 
                             ' bola_4, bola_5, bola_6, bola_7, bola_8, bola_9, bola_10, bola_11, bola_12, bola_13, ' + 
                             ' bola_14, bola_15, ganhadores_15, ganhadores_14, ganhadores_13, ganhadores_12, ganhadores_11) ' + 
                             ' values (%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)'
            % (
            int(concurso),
            int(dia),
            int(mes),
            int(ano),
            int(bo[0]), int(bo[1]), int(bo[2]), int(bo[3]), int(bo[4]), int(bo[5]), int(bo[6]), int(bo[7]), 
            int(bo[8]), int(bo[9]), int(bo[10]), int(bo[11]), int(bo[12]), int(bo[13]), int(bo[14]),
            int(ganhadores_15),
            int(ganhadores_14),
            int(ganhadores_13),
            int(ganhadores_12),
            int(ganhadores_11)))
            r = []

