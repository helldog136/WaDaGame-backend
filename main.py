from flask import Flask, request, Response

import database
import analyser
import os

app = Flask(__name__)

db = database.Database()

@app.route('/<appId>', methods=['POST'])
def addImage(appId):
    if request.headers['Content-Type'] == 'application/octet-stream':
        # Retreive the frame
        f = open('./'+str(appId)+'.jpg', 'wb')
        f.write(request.data)
        f.close()

        # Get the tag
        tag = analyser.getResult("./"+str(appId)+".jpg")

        # Add the tag to current DB
        res = db.addData(appId, tag, 0.6)

        # Remove no longer useful file
        os.remove("./"+str(appId)+".jpg")
        return Response(status=200, response="{\"confidence\":"+str(res)+"}")

    return Response(status=400, response="Wrong Content-Type")


@app.route('/<appId>', methods=['GET'])
def getResult(appId):
    if db.hasClient(appId):
        info = db.getResults(appId)
        t, c = db.removeClient(appId)
        return Response(status=200, response="{\"highest\":{\"tag\":\"" + str(t) + "\", \"certitude\":"
                                         + str(c) + "},\"detail\":" + str(info) + "}")
    else:
        return Response(status=404, response="ClientID not found, maybe you forgot to send images for analysis before?")


app.run(port=4242)

