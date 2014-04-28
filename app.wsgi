import sys, os, bottle
from server import app

# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

application = app
#application = bottle.default_app()