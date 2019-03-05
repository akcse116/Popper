from bottle import route, run, get, post, template, static_file
import JSMethods

@get('/')
def index():
    return static_file('index.html', root='')


@get('/style.css')
def stylesheets():
    return static_file('style.css', root='')


@get('/main.js')
def javascript():
    return static_file('main.js', root='')


@get('/sprites')
def sprites():
    return static_file('sprites.png', root='')


@get('/api')
def api():
    return static_file('gameState.json', root='')


@post('/updateState/<current>')  # Needs Further Expansion
def gameUpdate(current):
    filename = 'gameState.json'
    JSMethods.saveGameState(JSMethods.toJson(current), filename)


run(host='127.0.0.1', port=8080)
