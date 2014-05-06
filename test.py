import sys

sys.path.append('analise/')
sys.path.append('base_dados/')
sys.path.append('leitura/')
sys.path.append('pergunta/')
sys.path.append('gerador/')

#print (sys.path)

from leitura.leitor import leitor
from analise.analisador import analisador
from gerador.geradorjogo import GeradorJogo
from pergunta.pergunta import pergunta

#A tabela ja esta criada
#l = leitor()
#l.drop_table()
#l.create_table()
#l.extrair_dados()

a = analisador()
g = GeradorJogo()
p = pergunta()

print("randomico_com_melhores_repeticoes")
r = g.randomico_com_melhores_repeticoes(p)
print(r)

print("randomico_com_melhores_colunas")
r = g.randomico_com_melhores_colunas(p)
print(r)


#a.analisar_jogo([8, 9, 15, 21, 16, 18, 2, 4, 13, 23,1, 22, 10, 14, 19])
#a.analisar_jogo([11, 2, 1, 13, 19, 15, 25, 4, 12, 23, 24, 9, 17, 14, 20])
#a.analisar_jogo([18,20,25,23,10,11,24,14,6,2,13,9,5,16,3,5])
#a.coluna_com_mais_repeticao()


#jogo1 = g.randomico()
#print jogo1
#a.analisar_percentual_chance_jogo(jogo1)
#jogo2 = g.randomico_com_melhores_repeticoes(a)
#print jogo2
#a.analisar_percentual_chance_jogo(jogo2)

#jogo3 = g.jogo_com_percentual_de(a, 50)
#print jogo3
