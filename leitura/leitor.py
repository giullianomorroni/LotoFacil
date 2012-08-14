# -*- coding: utf-8 -*-
import sys
from pysqlite2 import dbapi2 as sqlite

#Esta classe serve para ler o resultado e armazenar na base
class leitor:

    global repeticoesNumero;

    def __init__(self):
        self.con = sqlite.connect('/opt/lotofacil/sqlite/lotofacil')

    def commit(self):
        self.con.commit()

    def extrair_dados(self):
        resultados = open('/opt/lotofacil/sqlite/resultados.txt')
        while (True):
            linha = resultados.readline();
            if len(linha) == 0: break;
            self.adicionar_linha(linha)
        self.commit();  

    def drop_table(self):
        try:
            self.con.execute('drop table loto')
        except Exception:
            print 'A tabela nao existe'      

    def create_table(self):
        self.con.execute(
                         ' create table loto (concurso, dia, mes, ano, bola_1, bola_2, bola_3,' + 
                         ' bola_4, bola_5, bola_6, bola_7, bola_8, bola_9, bola_10, bola_11, bola_12, bola_13, ' + 
                         ' bola_14, bola_15, ganhadores_15, ganhadores_14, ganhadores_13, ganhadores_12, ganhadores_11)')


    def adicionar_linha(self, linha):
        r = linha.split('#');
        data = r[1]
        concurso = r[0]
        dia = data.split('/')[0]
        mes = data.split('/')[1]
        ano = data.split('/')[2]
        ganhadores_15 = r[17]
        ganhadores_14 = r[18]	
        ganhadores_13 = r[19]
        ganhadores_12 = r[20]
        ganhadores_11 = r[21]

        self.con.execute('insert into loto (concurso, dia, mes, ano, bola_1, bola_2, bola_3,' + 
                         ' bola_4, bola_5, bola_6, bola_7, bola_8, bola_9, bola_10, bola_11, bola_12, bola_13, ' + 
                         ' bola_14, bola_15, ganhadores_15, ganhadores_14, ganhadores_13, ganhadores_12, ganhadores_11) ' + 
                         ' values (%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)'
        % (
        int(concurso),
        int(dia),
        int(mes),
        int(ano),
        int(r[2]), int(r[3]), int(r[4]), int(r[5]), int(r[6]), int(r[7]), int(r[8]), int(r[9]),
        int(r[10]), int(r[11]), int(r[12]), int(r[13]), int(r[14]), int(r[15]), int(r[16]),
        int(ganhadores_15),
        int(ganhadores_14),
        int(ganhadores_13),
        int(ganhadores_12),
        int(ganhadores_11)))
