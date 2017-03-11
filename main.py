from flask import Flask, request

app = Flask(__name__)


@app.route('/<appId>', methods=['POST'])
def addImage(appId):
    if request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./'+str(appId)+'.jpg', 'wb')
        f.write(request.data)
        f.close()


@app.route('/<appId>', methods=['GET'])
def getResult(appId):
    pass


app.run(port=4242)

print "hello world"
