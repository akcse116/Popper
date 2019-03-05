from bottle import route, run, get, post, template, static_file
import JSMethods

@route('/')
def index():
    return static_file('index.html', root='')


@route('/style.css')
def stylesheets():
    return static_file('style.css', root='')


@route('/main.js')
def javascript():
    return static_file('main.js', root='')


@route('/sprites')
def sprites():
    return static_file('sprites.png', root='')


@route('/api')
def api():
    filename = 'gameState.json'
    return JSMethods.getGameState(filename)
    # return static_file('gameState.json', root='')


@post('/updateState/<current>')  # Needs Further Expansion
def gameUpdate(current):
    filename = 'gameState.json'
    JSMethods.saveGameState(JSMethods.toJson(current), filename)


run(host='127.0.0.1', port=8080)
