# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

import bottle
from server import app

application = app
#application = bottle.default_app()