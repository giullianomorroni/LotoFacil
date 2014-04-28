'''
Created on 08/08/2012

@author: giulliano
'''

from base_dados.consulta import consulta
from collections import Counter
import sys

class analisador(object):

    c1 = [21,22,23,24,25]
    c2 = [16,17,18,19,20]
    c3 = [11,12,13,14,15]
    c4 = [6,7,8,9,10]
    c5 = [1,2,3,4,5]
 
    def analisar_probabilidade_jogo(self, jogo):
        jogo_repetido = 0;
        r = consulta().consulta_ano_mes()
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
