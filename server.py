from bottle import get, view, route, run, template, static_file

from gerador.geradorjogo import GeradorJogo
from analise.analisador import analisador
from pergunta.pergunta import pergunta

import sys

sys.path.append('analise/')
sys.path.append('base_dados/')
sys.path.append('leitura/')
sys.path.append('pergunta/')
sys.path.append('gerador/')

@route('/')
@view('index')
def index():
    return dict()

@get('/estoucomsorte')
def luckguy():
    g = GeradorJogo()
    a = analisador()
    jogo = g.randomico()
    analise = a.analisar_probabilidade_jogo(jogo)
    return dict(magic_numbers=list(jogo), percent=analise)

@get('/pastelaria/<pedido>')
def mount(pedido):
    g = GeradorJogo()
    a = analisador()
    p = pergunta()
    jogo = None;
    analise = None;
    if pedido == 'melhores_repeticoes':
        jogo = g.randomico_com_melhores_repeticoes(p)
    if pedido == 'melhores_colunas':
        jogo = g.randomico_com_melhores_colunas(p)
    if pedido == 'percentual':
        #pegar probabilidade desejada
        jogo = g.jogo_com_percentual_de(a, p, 25)
    if pedido == 'complete':
        #pegar jogo do cara
        jogo = g.completar_jogo([1,2,3,4,5])
    if pedido == 'aleatorio':
        jogo = g.randomico()
    analise = a.analisar_probabilidade_jogo(jogo)
    return dict(magic_numbers=list(jogo), percent=analise)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/Development/LotoFacil/views/bootstrap/')
    #return static_file(filepath, root='/opt/development/workspace/python/LotoFacil/views/bootstrap/')

run(host='0.0.0.0', port=9200)
