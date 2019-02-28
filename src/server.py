from bottle import route, run, template, static_file

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
    return


run(host='127.0.0.1', port=8080)