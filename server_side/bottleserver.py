import bottle, hashlib
import cartesian 
from bottle import route, run, template, request

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/login')
def login():
    return '''
       <form action="/upload" method="post" enctype="multipart/form-data">
       Select a file: <input type="file" name="data" />
       <input type="submit" value="Start upload" />
       </form>
       '''

@route('/upload', method = 'POST')
def do_upload():
        data = request.files.data
        raw = data.file.read()
        hash = hashlib.sha1(raw).hexdigest()
        print hash
        string = raw
        cartesian.decode(string,hash)
#       read.check(data)
run(host='localhost', port=8080)
