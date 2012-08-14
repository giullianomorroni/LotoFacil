'''
Created on 08/08/2012

@author: giulliano
'''
from pysqlite2 import dbapi2 as sqlite
from collections import Counter
import sys

class analisador(object):

    c1 = [21,22,23,24,25]
    c2 = [16,17,18,19,20]
    c3 = [11,12,13,14,15]
    c4 = [6,7,8,9,10]
    c5 = [1,2,3,4,5]

    def __init__(self):
        self.con = sqlite.connect('/opt/lotofacil/sqlite/lotofacil')

    def consulta(self, mes=1, ano=1990):
        r = self.con.execute('select bola_1, bola_2, bola_3,' + 
            ' bola_4, bola_5, bola_6, bola_7, bola_8, bola_9, bola_10, bola_11, bola_12, bola_13, ' + 
            ' bola_14, bola_15 from loto where ano > %d and mes > %d' % (ano, mes))
        return r

    def melhor_repeticao_numeros(self, quantidade=5, mes=1, ano=1990):
        r = self.consulta(mes, ano);
        cnt = Counter();
        for bolas in r:
            for bola in bolas:
                if quantidade == 0: break;
                cnt[bola] +=1
                quantidade -= 1
        return cnt

    def coluna_com_mais_repeticao(self):
        r = self.consulta();
        cnt = Counter();
        for bolas in r:
            for bola in bolas:
                if bola <= 5:
                    cnt['coluna 1'] +=1
                if bola >= 6 and bola <= 10:
                    cnt['coluna 2'] +=1
                if bola >= 11 and bola <= 15:
                    cnt['coluna 3'] +=1
                if bola >= 16 and bola <= 20:
                    cnt['coluna 4'] +=1
                if bola >= 21 and bola <= 20:
                    cnt['coluna 5'] +=1

        return cnt

    def melhor_repeticao_numeros_por_coluna(self, coluna=5):
        r = self.consulta();
        cnt = Counter();
        for bolas in r:
            for bola in bolas:
                if coluna == 1 and bola in self.c1:
                    cnt[bola] +=1
                if coluna == 2 and bola in self.c2:
                    cnt[bola] +=1
                if coluna == 3 and bola in self.c3:
                    cnt[bola] +=1
                if coluna == 4 and bola in self.c4:
                    cnt[bola] +=1
                if coluna == 5 and bola in self.c5:
                    cnt[bola] +=1                
        return cnt

    def analisar_percentual_chance_jogo(self, jogo):
        jogo_repetido = 0;
        r = self.consulta()
        cnt = Counter();
        for bolas in r:
            if (jogo_repetido == 15):
                print 'Este jogo ja foi sorteado %s !!!!!' %bolas
                sys.exit(-1);
            jogo_repetido = 0;
          
            for bola in bolas:
                cnt[bola] +=1
                if bola in jogo:
                    jogo_repetido += 1
        mc = cnt.most_common(15)

        #Se a bola esta dentro das melhores repoticoes, soma-se um (1/3)/15
        ttl = 0;
        for b in mc: 
            if b[0] in jogo:
                ttl += (33/15)
        bom_jogo = (ttl)

        #Se tiver ao menos 3 numeros com as melhores repeticoes por coluna, soma-se um (1/3)/15
        rc1 = [i for i in jogo if i in self.c1]
        rc2 = [i for i in jogo if i in self.c2]
        rc3 = [i for i in jogo if i in self.c3]
        rc4 = [i for i in jogo if i in self.c4]
        rc5 = [i for i in jogo if i in self.c5]

        por_coluna = len(rc1) > 3 or len(rc2) > 3 or len(rc3) > 3 or len(rc4) > 3 or len(rc5) > 3
        if por_coluna == True:
            bom_jogo = (bom_jogo + (33))

        print 'Seu jogo possuim um percentual de acerto de %s ' %bom_jogo
        return bom_jogo;
