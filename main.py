from flask import Flask, request

app = Flask(__name__)

@app.route('/<appId>', methods = ['POST'])
def addImage(appId):
    if request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./appID.jpg', 'wb')
        f.write(request.data)
        f.close()


app.run(port=4242)

print "hello world"