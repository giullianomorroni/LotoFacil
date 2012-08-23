# -*- coding: utf-8 -*-
import sys
import os
from pysqlite2 import dbapi2 as sqlite
from collections import deque

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
            os.remove('/opt/lotofacil/sqlite/lotofacil')
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
