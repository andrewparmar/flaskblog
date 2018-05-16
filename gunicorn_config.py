import os

port = int(os.environ.get('PORT', 5000))
bind = "0.0.0.0:{}".format(port)
workers = 2
