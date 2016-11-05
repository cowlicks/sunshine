#!/home/public/cgi-bin/sunshine-env/bin/python
from wsgiref.handlers import CGIHandler
from sunshine import app

CGIHandler().run(app)
