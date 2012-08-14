'''
Created on 11/08/2012

@author: giulliano
'''

from random import uniform
from collections import deque

class GeradorJogo(object):

    def __init__(self):
        pass

    def randomico(self):
        jogo = deque()
        while len(jogo) != 15: 
            bola = int(uniform(1,25))
            if bola not in jogo:
                jogo.append(bola)
        return jogo;

    def completar_jogo(self, jogo):
        if len(jogo) == 15:
            return jogo

        if len(jogo) > 15:
            novo_jogo = deque()
            for j in range(15):
                novo_jogo.append(jogo[j])
            return novo_jogo

        while len(jogo) < 15:
            bola = int(uniform(1,25))
            if bola not in jogo:
                jogo.append(bola)

        return jogo;

    def randomico_com_melhores_repeticoes(self, analisador, repeticoes=7):
        jogo = deque()
        bolas = analisador.melhor_repeticao_numeros(repeticoes);
        for melhores in bolas:
            jogo.append(melhores)
        return jogo;

    def randomico_com_melhores_colunas(self, analisador, coluna=2):
        jogo = deque()
        bolas = analisador.melhor_repeticao_numeros_por_coluna(coluna);
        for melhores in bolas:
            jogo.append(melhores)
        return jogo;

    def jogo_com_percentual_de(self, analisador, percentual):
        p = 0
        while (p < percentual):
            jogo = deque()
            x = int(uniform(1,5))
            ca = int(uniform(1,5))
            jogo1 = self.randomico_com_melhores_repeticoes(analisador, x)
            jogo2 = self.randomico_com_melhores_colunas(analisador, ca)

            aux = [j for j in jogo1]
            aux += [j for j in jogo2]

            for j in aux:
                if j not in jogo:
                    jogo.append(j)

            jogo = self.completar_jogo(jogo);
            sorted(jogo)
            p = analisador.analisar_percentual_chance_jogo(jogo)
        return jogo;