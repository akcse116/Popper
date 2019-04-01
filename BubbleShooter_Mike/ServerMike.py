import bottle
from bottle import route, run, get, post, template

@bottle.route("/")
def hello():
    response=("HELLO")
    return response


bottle.run(host='0.0.0.0', port=8080, debug=True)
