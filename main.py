from bottle import route, run, request, static_file, template, get, post

contacts = [
    {'name': 'John', 'surname': 'Doe', 'phone-number': '870007078979', 'address': 'Abay 1', },
    {'name': 'Sam', 'surname': 'Smith', 'phone-number': '87777899456', 'address': 'Esil 27', },
]

messages = []

@get('/contact_us')
def contact_us_get():
    return template("contact_us.html", root='./')

@post('/contact_us')
def contact_us_post():
    messages.append({
        'name': request['name'],
        'phone': request['phone'],
        'message': request['message']
    })

@route('/phonebook')
def phonebook():
    return template("phonebook.html", root='./', contacts=contacts)


@route('/home')
def hello():
    return template("index.html", root='./')


@route('/master.css')
def masterCss():
    return static_file("master.css", root="./")


run(host="localhost", port=8080, debug=True)
