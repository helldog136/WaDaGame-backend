from flask import Flask, request, Response

import database

app = Flask(__name__)

db = database.Database()

@app.route('/<appId>', methods=['POST'])
def addImage(appId):
    if request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./'+str(appId)+'.jpg', 'wb')
        f.write(request.data)
        f.close()
    return Response(status=200, response="OK")


@app.route('/<appId>', methods=['GET'])
def getResult(appId):
    info = db.getResults(appId)
    t, c = db.removeClient(appId)
    return Response(status=200, response="{\"highest\":{\"tag\":\""+t+"\", \"certitude\":"+c+"},\"detail\":"+str(info)+"}")


app.run(port=4242)

print "hello world"
