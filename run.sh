#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append('/media/Desenvolvimento/workspace/python/LotoFacil/analise/')
sys.path.append('/media/Desenvolvimento/workspace/python/LotoFacil/base_dados/')
sys.path.append('/media/Desenvolvimento/workspace/python/LotoFacil/leitura/')
sys.path.append('/media/Desenvolvimento/workspace/python/LotoFacil/pergunta/')
sys.path.append('/media/Desenvolvimento/workspace/python/LotoFacil/gerador/')

print sys.path

#from leitura.leitor import leitor
#from analise.analisador import analisador
#from gerador.geradorjogo import GeradorJogo

#A tabela ja esta criada
#l = leitor()
#l.drop_table()
#l.create_table()
#l.extrair_dados()

#a = analisador()
#a.melhor_repeticao_numeros(15)
#a.melhor_repeticao_numeros_por_coluna()
#a.analisar_jogo([8, 9, 15, 21, 16, 18, 2, 4, 13, 23,1, 22, 10, 14, 19])
#a.analisar_jogo([11, 2, 1, 13, 19, 15, 25, 4, 12, 23, 24, 9, 17, 14, 20])
#a.analisar_jogo([18,20,25,23,10,11,24,14,6,2,13,9,5,16,3,5])
#a.coluna_com_mais_repeticao()

#g = GeradorJogo()
#a = analisador()

#jogo1 = g.randomico()
#print jogo1
#a.analisar_percentual_chance_jogo(jogo1)
#jogo2 = g.randomico_com_melhores_repeticoes(a)
#print jogo2
#a.analisar_percentual_chance_jogo(jogo2)

#jogo3 = g.jogo_com_percentual_de(a, 50)
#print jogo3
