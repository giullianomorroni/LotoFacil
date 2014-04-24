from bottle import get, view, route, run, template, static_file

from gerador.geradorjogo import GeradorJogo
import sys

sys.path.append('analise/')
sys.path.append('base_dados/')
sys.path.append('leitura/')
sys.path.append('pergunta/')
sys.path.append('gerador/')

@route('/hello/<name>')
def index(name):
    return template('<b>NCR {{name}}</b>!', name=name)

@get('/estoucomsorte/')
@view('luckguy')
def luckguy():
    g = GeradorJogo()
    jogo = g.randomico()
    return dict(magic_numbers=jogo)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/Development/LotoFacil/views/bootstrap-3.1.1/')

run(host='localhost', port=8080)
