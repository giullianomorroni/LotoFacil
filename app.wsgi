import sys, os, bottle

path = '/var/www/LotoFacil/'
sys.path.append(path)

os.chdir('/var/www/LotoFacil/')

#my *.py that handle get/post
import server

application = bottle.default_app()