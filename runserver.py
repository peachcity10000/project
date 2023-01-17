import os
from flask import *
from peach10000 import app



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.debug = True
    app.run(host='0.0.0.0', port=port)

