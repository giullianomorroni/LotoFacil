import sys, os, bottle

path = '/var/www/LotoFacil/'
sys.path.append(path)

os.chdir('/var/www/LotoFacil/')
application = bottle.default_app()