from bottle import route, run, request

@route('/message')
def hello():
    return "Hello world"

run(host="localhost", port=8080, debug=True)