import sys
sys.psth.insert(0, 'C:\Users\Kamaraj\Desktop\APP')

from flet import app

def application(environ,start_response):
    result = app.run(environ['wsgi.input'], environ)
    start_response('200 OK', [('Content-type', 'text/html')])
    return [result.encode()]