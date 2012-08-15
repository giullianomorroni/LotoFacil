'''
Created on 14/08/2012

@author: giulliano
'''

from base_dados.consulta import consulta
from collections import Counter

class pergunta(object):

    c1 = [21,22,23,24,25]
    c2 = [16,17,18,19,20]
    c3 = [11,12,13,14,15]
    c4 = [6,7,8,9,10]
    c5 = [1,2,3,4,5]

    def repeticao_numeros(self, quantidade=5, mes=1, ano=1990):
        r = consulta().consulta_ano_mes(mes, ano);
        cnt = Counter();
        for bolas in r:
            for bola in bolas:
                cnt[bola] +=1
        return cnt.most_common(quantidade)

    def repeticao_numeros_coluna(self, coluna, mes=1, ano=1990):
        r = consulta().consulta_ano_mes(mes, ano)
        cnt = Counter();
        for bolas in r:
            for bola in bolas:
                if bola <= 5:
                    cnt[bola] +=1
                if bola >= 6 and bola <= 10:
                    cnt[bola] +=1
                if bola >= 11 and bola <= 15:
                    cnt[bola] +=1
                if bola >= 16 and bola <= 20:
                    cnt[bola] +=1
                if bola >= 21 and bola <= 20:
                    cnt[bola] +=1

        if coluna != None:
            if coluna == 1:
                return [x for x in cnt if x in self.c1]
            if coluna == 2:
                return [x for x in cnt if x in self.c2]
            if coluna == 3:
                return [x for x in cnt if x in self.c3]
            if coluna == 4:
                return [x for x in cnt if x in self.c4]
            if coluna == 5:
                return [x for x in cnt if x in self.c5]            
        return cnt

    def repeticao_colunas(self, coluna, mes=1, ano=1990):
        r = consulta().consulta_ano_mes(mes, ano)
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
